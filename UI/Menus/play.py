import sys
from pathlib import Path

import cv2
import importlib
import importlib.util

from Backend.RankingDAO import RankingsDAO
from Sprites.fruit import Fruit
from UI.Button import Button
from app import Game

from Config.window_config import *

from UI.Text import Text

from Controllers.Audio import GeneralSFX

from Sprites.perfect_overlay import PerfectOverlay
from Sprites.good_overlay import GoodOverlay
from Sprites.checkpoint_star import CheckpointStar

from Sprites.player import Player


class Play:
    def __init__(self, camera, song, asset_loader, player_info):
        self.camera = camera
        self.song = song
        self.asset_loader = asset_loader
        self.player_info = player_info

    def run(self):
        file_path = Path(f"Songs/{self.song.song_name}/controller.py")
        module_name = "controller_module"
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        controller = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = controller
        spec.loader.exec_module(controller)

        GeneralSFX.stop_current()
        base_game = BaseGame(camera=self.camera, asset_loader=self.asset_loader,
                             song=self.song, controller=controller)

        standby_screen = StandbyScreen(game=base_game)
        standby_screen.run()

        main_game = MainGame(game=base_game)
        main_game.run()

        if base_game.go_to == 'Scoreboard':
            scoreboard = Scoreboard(player=main_game.player, game=base_game, player_info=self.player_info)
            scoreboard.run()

        return base_game.go_to


class BaseGame:
    def __init__(self, camera, asset_loader, song, controller):

        self.camera = camera
        self.asset_loader = asset_loader
        self.song = song
        self.controller = controller

        self.all_sprites = pygame.sprite.Group()
        self.left_fruits_sprites = pygame.sprite.Group()
        self.right_fruits_sprites = pygame.sprite.Group()

        self.background_frame_counter = 0
        self.background_frame_interval = FPS / self.song.songs_fps
        self.background_video = self.asset_loader.assets[self.song.song_name]
        self.background_last_frame = None

        self.perfect_overlay_left = PerfectOverlay(self.all_sprites, position=(WIDTH / 2 - 240, HEIGHT - 100))
        self.perfect_overlay_right = PerfectOverlay(self.all_sprites, position=(WIDTH / 2 + 240, HEIGHT - 100))

        self.good_overlay_left = GoodOverlay(self.all_sprites, position=(
            (self.perfect_overlay_left.rect.midleft[0] - 50), self.perfect_overlay_left.rect.midleft[1]))
        self.good_overlay_right = GoodOverlay(self.all_sprites, position=(
            (self.perfect_overlay_right.rect.midright[0] + 50), self.perfect_overlay_right.rect.midright[1]))

        self.game_start = True
        self.game_ended = False
        self.game_paused = False

        self.go_to = None

    def draw_background(self, display_static=False):
        if self.background_frame_counter % self.background_frame_interval == 0:

            ret, frame = self.background_video.read()

            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                frame_surface = pygame.surfarray.make_surface(frame)
                frame_surface = pygame.transform.rotate(frame_surface, -90)
                frame_surface = pygame.transform.flip(frame_surface, True, False)
                frame_surface = pygame.transform.scale(frame_surface, (WIDTH, HEIGHT))

                self.background_last_frame = frame_surface
            else:
                self.background_video.set(cv2.CAP_PROP_POS_FRAMES, 0)

            self.camera.internal_surface.blit(self.background_last_frame, (0, 0))

        if not display_static:
            self.background_frame_counter += 1.0
        else:
            self.background_video.set(cv2.CAP_PROP_POS_FRAMES, 0)

    def go_back_to_main_menu(self):
        self.game_start = False
        self.game_paused = False
        self.go_to = "Main"

    def restart(self):
        self.game_start = False
        self.game_paused = False
        self.go_to = "Play"


class StandbyScreen:
    def __init__(self, game):
        self.game = game
        self.innit_text = Text(msg=f"Pressione os dois lados do mouse para começar", position=(WIDTH / 2, 100),
                               color=WHITE, font_size=40, centered=True)

    def run(self):
        while True:
            CLOCK.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.game.draw_background(display_static=True)
            self.innit_text.draw(self.game.camera.internal_surface)

            mouse_buttons = pygame.mouse.get_pressed()
            if mouse_buttons[0] and mouse_buttons[2]:
                break

            self.game.all_sprites.update(self.game.perfect_overlay_left, self.game.perfect_overlay_right)
            self.game.all_sprites.draw(self.game.camera.internal_surface)

            Game.blit_screen(self.game.camera)
            pygame.display.flip()


class MainGame:
    def __init__(self, game):
        self.game = game

        self.games_fps = FPS

        self.current_song_level = 0

        self.slow_motion_counter = 0
        self.should_slow_down = False
        self.slow_motion_activation_index = 0
        self.slow_motion_activation_counter = 0

        self.player = Player(self.game.all_sprites, all_sprites=self.game.all_sprites,
                             perfect_overlay_left=self.game.perfect_overlay_left,
                             perfect_overlay_right=self.game.perfect_overlay_right,
                             good_overlay_left=self.game.good_overlay_left,
                             good_overlay_right=self.game.good_overlay_right,
                             left_fruit_sprites=self.game.left_fruits_sprites,
                             right_fruit_sprites=self.game.right_fruits_sprites,
                             asset_loader=self.game.asset_loader,
                             game_panel=self)
        self.player_dead_counter = 0

        self.spawn_fruits_event_triggers = {}
        self.increase_speed_event_triggers = []
        self.pulse_camera_event_triggers = []

        self.song_dict = self.game.controller.song()

    def run(self):
        GeneralSFX.play_song(self.game.song.song_name, loops=1, start=147)

        self.populate_spawn_fruits_event_triggers(self.song_dict.keys(), delay=147000)
        self.populate_increase_speed_event_triggers(self.game.controller.level_increase_timestamps(), delay=147000)
        self.populate_camera_pulse_event_triggers(self.game.controller.pulse_camera_timestamps(), delay=147000)

        music_start_time = pygame.time.get_ticks()

        fade_duration = 5000
        fade_alpha = 0
        fade_speed = 255 / (fade_duration / self.games_fps)

        while self.game.game_start:
            CLOCK.tick(self.games_fps)

            if self.should_slow_down:
                self.slow_motion_counter += 1

            if self.player.is_player_dead:
                self.player_dead_counter += 1

            if self.slow_motion_counter > self.games_fps * 5 or self.player_dead_counter > self.games_fps * 3:
                self.deactivate_slow_motion()
                self.game.game_ended = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type in self.spawn_fruits_event_triggers.keys():
                    timestamp = self.spawn_fruits_event_triggers[event.type]
                    fruit_dict = self.song_dict[timestamp]

                    is_double = fruit_dict['double']
                    is_last_fruit = self.game.controller.last_timestamp() == timestamp

                    if is_last_fruit:
                        self.slow_motion_activation_index = 2 if is_double else 1

                    if is_double:
                        if fruit_dict.get('checkpoint'):
                            CheckpointStar(
                                (self.game.all_sprites, self.game.left_fruits_sprites),
                                all_sprites=self.game.all_sprites,
                                side_to_spawn='Left',
                                current_level=self.current_song_level,
                                asset_loader=self.game.asset_loader,
                                game_panel=self,
                                is_last_fruit=is_last_fruit,
                            )
                            CheckpointStar(
                                (self.game.all_sprites, self.game.right_fruits_sprites),
                                all_sprites=self.game.all_sprites,
                                side_to_spawn='Right',
                                current_level=self.current_song_level,
                                asset_loader=self.game.asset_loader,
                                game_panel=self,
                                is_last_fruit=is_last_fruit,
                            )
                        else:
                            Fruit(
                                (self.game.all_sprites, self.game.left_fruits_sprites),
                                side_to_spawn='Left',
                                is_long=fruit_dict['is_long'],
                                health=fruit_dict['health'],
                                current_level=self.current_song_level,
                                perfect_overlay_left=self.game.perfect_overlay_left,
                                perfect_overlay_right=self.game.perfect_overlay_right,
                                asset_loader=self.game.asset_loader,
                                all_sprites=self.game.all_sprites,
                                is_last_fruit=is_last_fruit,
                                game_panel=self,
                            ),
                            Fruit(
                                (self.game.all_sprites, self.game.right_fruits_sprites),
                                side_to_spawn='Right',
                                is_long=fruit_dict['is_long'],
                                health=fruit_dict['health'],
                                current_level=self.current_song_level,
                                perfect_overlay_left=self.game.perfect_overlay_left,
                                perfect_overlay_right=self.game.perfect_overlay_right,
                                asset_loader=self.game.asset_loader,
                                all_sprites=self.game.all_sprites,
                                is_last_fruit=is_last_fruit,
                                game_panel=self,
                            )
                    else:
                        belong_to_sprite = self.game.left_fruits_sprites if fruit_dict[
                                                                                'side_to_spawn'] == 'Left' else self.game.right_fruits_sprites
                        if fruit_dict.get('checkpoint'):
                            CheckpointStar(
                                (self.game.all_sprites, belong_to_sprite),
                                all_sprites=self.game.all_sprites,
                                side_to_spawn=fruit_dict['side_to_spawn'],
                                current_level=self.current_song_level,
                                asset_loader=self.game.asset_loader,
                                game_panel=self,
                                is_last_fruit=self.game.controller.last_timestamp() == timestamp,
                            )
                        else:
                            Fruit(
                                (self.game.all_sprites, belong_to_sprite),
                                side_to_spawn=fruit_dict['side_to_spawn'],
                                is_long=fruit_dict['is_long'],
                                health=fruit_dict['health'],
                                current_level=self.current_song_level,
                                perfect_overlay_left=self.game.perfect_overlay_left,
                                perfect_overlay_right=self.game.perfect_overlay_right,
                                asset_loader=self.game.asset_loader,
                                all_sprites=self.game.all_sprites,
                                is_last_fruit=self.game.controller.last_timestamp() == timestamp,
                                game_panel=self,
                            )
                elif event.type in self.increase_speed_event_triggers:
                    self.current_song_level += 1
                    print('Song speed increased')

                elif event.type in self.pulse_camera_event_triggers:
                    if not self.should_slow_down:
                        first_zoom = 1 + (self.current_song_level / 100)
                        self.game.camera.setup_pulse(first_zoom, 10)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game.game_paused = True
                        music_start_time += self.pause_menu(self.song_dict.keys(),
                                                            delay=pygame.time.get_ticks() - music_start_time,
                                                            increase_speed_timestamps=self.game.controller.level_increase_timestamps(),
                                                            pulse_camera_timestamps=self.game.controller.pulse_camera_timestamps()
                                                            )

            self.game.draw_background(display_static=not self.game.game_start)
            self.display_player_health(screen=self.game.camera.internal_surface)
            self.game.all_sprites.update(self.game.perfect_overlay_left, self.game.perfect_overlay_right)
            self.game.all_sprites.draw(self.game.camera.internal_surface)

            if self.game.game_ended:
                fade_alpha = min(fade_alpha + fade_speed, 255)
                fade_surface = pygame.Surface((WIDTH, HEIGHT))
                fade_surface.fill((0, 0, 0))
                fade_surface.set_alpha(int(fade_alpha))
                self.game.camera.internal_surface.blit(fade_surface, (0, 0))

            Fruit.slash_audio_counter += 1

            self.game.camera.pulse()

            Game.blit_screen(self.game.camera, align_with_player=self.should_slow_down)
            pygame.display.flip()

            if self.game.game_ended and fade_alpha >= 255:
                self.game.go_to = 'Scoreboard'
                self.game.game_start = False

    def activate_slow_motion(self):
        self.slow_motion_activation_counter += 1
        if self.slow_motion_activation_index == self.slow_motion_activation_counter:
            self.should_slow_down = True
            self.slow_motion_counter = 0
            self.games_fps = 8

            self.game.camera.zoom_scale = 2

            audio = self.game.asset_loader.assets['sounds']['slow_motion']
            audio.play()

    def deactivate_slow_motion(self):
        self.should_slow_down = False
        self.slow_motion_counter = 0
        self.slow_motion_activation_index = 0
        self.slow_motion_activation_counter = 0
        self.games_fps = FPS

    def populate_spawn_fruits_event_triggers(self, timestamps, delay=0):
        self.spawn_fruits_event_triggers = {}
        for timestamp in timestamps:
            event_trigger = pygame.event.custom_type()
            pygame.time.set_timer(event_trigger, timestamp - 1000 - delay, loops=1)
            self.spawn_fruits_event_triggers[event_trigger] = timestamp

    def populate_increase_speed_event_triggers(self, timestamps, delay=0):
        self.increase_speed_event_triggers = []
        for timestamp in timestamps:
            event_trigger = pygame.event.custom_type()
            pygame.time.set_timer(event_trigger, timestamp - delay, loops=1)
            self.increase_speed_event_triggers.append(event_trigger)

    def populate_camera_pulse_event_triggers(self, timestamps, delay=0):
        self.pulse_camera_event_triggers = []
        for timestamp in timestamps:
            event_trigger = pygame.event.custom_type()
            pygame.time.set_timer(event_trigger, timestamp - delay, loops=1)
            self.pulse_camera_event_triggers.append(event_trigger)

    def pause_menu(self, timestamps, delay, increase_speed_timestamps, pulse_camera_timestamps):
        GeneralSFX.pause_current()
        initial_time = pygame.time.get_ticks()

        go_back_button = Button(position=(WIDTH / 2, HEIGHT / 2 - 100), size=(200, 50), color=GRAY, font_color=WHITE,
                                hover_color=BLACK, on_click=self.game.go_back_to_main_menu,
                                text="Voltar ao menu principal")

        restart_button = Button(position=(WIDTH / 2, HEIGHT / 2 + 100), size=(200, 50), color=GRAY, font_color=WHITE,
                                hover_color=BLACK, on_click=self.game.restart,
                                text="Reiniciar tentativa")

        overlay = pygame.Surface(self.game.camera.internal_surface.get_size())
        overlay.fill(DARK_GRAY)
        overlay.set_alpha(12)

        while self.game.game_paused:
            CLOCK.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        GeneralSFX.resume_current()

                        self.populate_spawn_fruits_event_triggers(timestamps=timestamps, delay=delay)
                        self.populate_increase_speed_event_triggers(timestamps=increase_speed_timestamps, delay=delay)
                        self.populate_camera_pulse_event_triggers(timestamps=pulse_camera_timestamps, delay=delay)

                        self.game.game_paused = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if go_back_button.rect.collidepoint(event.pos):
                            go_back_button.handle_click()

                        elif restart_button.rect.collidepoint(event.pos):
                            restart_button.handle_click()

            self.game.camera.internal_surface.blit(overlay, (0, 0))

            go_back_button.draw(self.game.camera.internal_surface)
            restart_button.draw(self.game.camera.internal_surface)

            Game.blit_screen(self.game.camera)

            pygame.display.flip()

        return pygame.time.get_ticks() - initial_time

    def display_player_health(self, screen):
        container_width, container_height = 300, 50
        container_surf = pygame.Surface((container_width, container_height))
        container_rect = container_surf.get_rect(midtop=(WIDTH / 2 - 400, 150))

        pygame.draw.rect(container_surf, RED, (0, 0, (container_width * (self.player.health / 100)), container_height))
        pygame.draw.rect(container_surf, GRAY, container_surf.get_rect(), 2)
        screen.blit(container_surf, container_rect)


class Scoreboard:
    def __init__(self, player, game, player_info):
        self.player = player
        self.game = game
        self.player_info = player_info

        self.player.score += (self.player.perfects * 2 + self.player.goods) * (self.player.style_meter_peak / 100) * (
                self.player.health / 100) - self.player.misses * 5

        self.response = self.save_ranking()

        self.start_time = pygame.time.get_ticks()

        self.timer_for_final_score = 3000

        self.amount_to_add_initial_score = self.player.score / (FPS * (self.timer_for_final_score / 1000))

        self.label_text = Text(msg="SUA PONTUAÇÃO FINAL:", position=(50, 50), color=WHITE, font_size=40, centered=False)
        self.perfects_text = Text(msg=f"Perfeitos: {self.player.perfects}", position=(50, 150), color=GOLD,
                                  font_size=40,
                                  centered=False)
        self.goods_text = Text(msg=f"Boas: {self.player.goods}", position=(50, 200), color=GREEN, font_size=40,
                               centered=False)
        self.misses_text = Text(msg=f"Erros: {self.player.misses}", position=(50, 250), color=RED, font_size=40,
                                centered=False)
        self.style_meter_text = Text(msg=f"Pico do medidor de estilo: {self.player.style_meter_peak}%",
                                     position=(50, 300),
                                     color=WHITE, font_size=40, centered=False)
        self.health_text = Text(msg=f"Vida restante: {self.player.health}%", position=(50, 350), color=WHITE,
                                font_size=40,
                                centered=False)
        self.final_points = Text(msg="0", position=(50, HEIGHT - 130), color=YELLOW, font_size=80, centered=False)

        self.go_back_button = Button(position=(WIDTH - 50 - 75, HEIGHT - 50), size=(200, 50), color=GRAY,
                                     font_color=BLACK,
                                     hover_color=WHITE, on_click=self.game.go_back_to_main_menu,
                                     text="Voltar ao menu principal")

        self.restart_button = Button(position=(WIDTH - 75 - 50 - 50 - 200, HEIGHT - 50), size=(200, 50), color=GRAY,
                                     font_color=BLACK,
                                     hover_color=WHITE, on_click=self.game.restart,
                                     text="Tentar novamente")

        self.results_text = Text(msg=self.response['message'], position=(WIDTH * 0.80, HEIGHT - 150),
                                 color=self.response['color'],
                                 font_size=40, centered=True)

        self.event_trigger = pygame.event.custom_type()
        pygame.time.set_timer(self.event_trigger, self.timer_for_final_score + 3000, loops=1)

        self.go_to = None

    def run(self):
        while True:
            CLOCK.tick(FPS)
            elapsed_time = pygame.time.get_ticks() - self.start_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.go_back_button.rect.collidepoint(event.pos):
                            self.go_back_button.handle_click()
                            return self.go_to
                        elif self.restart_button.rect.collidepoint(event.pos):
                            self.restart_button.handle_click()
                            return self.go_to
                elif event.type == self.event_trigger:
                    sound = self.response['audio']
                    if sound is not None:
                        sound.play()

            self.game.draw_background(display_static=False)
            self.label_text.draw(self.game.camera.internal_surface)
            self.perfects_text.draw(self.game.camera.internal_surface)
            self.goods_text.draw(self.game.camera.internal_surface)
            self.misses_text.draw(self.game.camera.internal_surface)
            self.style_meter_text.draw(self.game.camera.internal_surface)
            self.health_text.draw(self.game.camera.internal_surface)

            if elapsed_time > self.timer_for_final_score:
                current_points = float(self.final_points.msg)
                if current_points < self.player.score:
                    current_points += self.amount_to_add_initial_score
                    self.final_points.msg = f"{current_points:.0f}"
                else:
                    self.go_back_button.draw(self.game.camera.internal_surface)
                    self.restart_button.draw(self.game.camera.internal_surface)
                    self.results_text.draw(self.game.camera.internal_surface)
                self.final_points.draw(self.game.camera.internal_surface)

            Game.blit_screen(self.game.camera)
            pygame.display.flip()

    def save_ranking(self):
        rankingsDAO = RankingsDAO()

        old_score = 0
        try:
            old_entry = rankingsDAO.get_ranking_by_music(self.game.song.song_name, self.player_info[0])
            if old_entry is not None:
                old_score = old_entry[2]
        except Exception as e:
            print(e)
        finally:
            print(f'old score: {old_score}')
            print(f'games score: {self.player.score}')

            if self.player.score > old_score:
                try:
                    rankingsDAO.add_ranking(self.game.song.song_name, self.player_info[0], self.player.score)
                except Exception as e:
                    print(e)
                finally:
                    entries = rankingsDAO.get_rankings_by_music("I Want It That Way")
                    first_row = entries[0]
                    first_row_score = first_row[2]

                    if first_row_score == self.player.score:
                        return {
                            'message': 'Novo recorde mundial',
                            'color': GOLD,
                            'audio': self.game.asset_loader.assets['sounds']['scores']['world_record']
                        }
                    else:
                        return {
                            'message': 'Novo recorde pessoal!',
                            'color': GREEN,
                            'audio': self.game.asset_loader.assets['sounds']['scores']['personal_record']
                        }

            return {
                'message': 'Nada mudou!',
                'color': WHITE,
                'audio': None,
            }
