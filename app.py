import pygame
pygame.init()
pygame.mixer.init()


import time
from random import randint
import cv2

from Config.window_config import *
from Config.colors import *
from Config.camera import Camera

from Sprites.player import Player
from Sprites.fruit import Fruit

from Sprites.perfect_overlay import PerfectOverlay
from Sprites.good_overlay import GoodOverlay


class Game:
    def __init__(self):
        camera = Camera()

        from UI.Menus.boot import Boot
        from UI.Menus.login import Login
        from UI.Menus.main import Main
        from UI.Menus.play import Play

        boot = Boot(camera=camera)
        asset_loader = boot.run()

        login = Login(camera=camera)
        main = Main(camera=camera, player=None, asset_loader=asset_loader)
        play = Play(camera=camera, song=None, asset_loader=asset_loader, player_info=None)

        running = True
        self.next_action = 'Login'

        while running:
            CLOCK.tick(FPS)
            match self.next_action:
                case 'Login':
                    response = login.run()
                    if response is not None:
                        main.player = response
                        play.player_info = response
                        self.next_action = 'Main'
                case 'Main':
                    response = main.run()
                    if response is not None:
                        play.song = response
                        self.next_action = 'Play'
                case 'Play':
                    self.next_action = play.run()

        current_level = 1

        all_sprites = pygame.sprite.Group()
        left_fruits_sprites = pygame.sprite.Group()
        right_fruits_sprites = pygame.sprite.Group()

        perfect_overlay_left = PerfectOverlay(all_sprites,
                                              position=(window_config.WIDTH / 2 - 240, window_config.HEIGHT - 100))
        perfect_overlay_right = PerfectOverlay(all_sprites,
                                               position=(window_config.WIDTH / 2 + 240, window_config.HEIGHT - 100))

        good_overlay_left = GoodOverlay(all_sprites, position=(
            (perfect_overlay_left.rect.midleft[0] - 50), perfect_overlay_left.rect.midleft[1]))
        good_overlay_right = GoodOverlay(all_sprites, position=(
            (perfect_overlay_right.rect.midright[0] + 50), perfect_overlay_right.rect.midright[1]))

        player = Player(all_sprites, all_sprites=all_sprites, perfect_overlay_left=perfect_overlay_left,
                        perfect_overlay_right=perfect_overlay_right, good_overlay_left=good_overlay_left,
                        good_overlay_right=good_overlay_right,
                        left_fruit_sprites=left_fruits_sprites, right_fruit_sprites=right_fruits_sprites,
                        asset_loader=asset_loader
                        )

        font = pygame.font.Font(None, 100)
        ghost_town = GhostTown()

        event_triggers = {}
        for timestamp in ghost_town.song.keys():
            event_trigger = pygame.event.custom_type()
            pygame.time.set_timer(event_trigger, timestamp, loops=1)
            event_triggers[event_trigger] = timestamp

        increase_speed_events = []
        for timestamp in ghost_town.increase_speed_timestamps:
            event_trigger = pygame.event.custom_type()
            pygame.time.set_timer(event_trigger, timestamp, loops=1)
            increase_speed_events.append(event_trigger)

        shake_camera_events = []
        for timestamp in ghost_town.shake_camera_timestamps:
            event_trigger = pygame.event.custom_type()
            pygame.time.set_timer(event_trigger, timestamp, loops=1)
            shake_camera_events.append(event_trigger)

        running = True

        def display_score(screen):
            text_surf = font.render(str(player.score), True, (240, 240, 240))
            text_rect = text_surf.get_rect(midtop=(window_config.WIDTH / 2, 50))
            screen.blit(text_surf, text_rect)

        def display_style_meter(screen):
            container_width, container_height = 200, 50
            container_surf = pygame.Surface((container_width, container_height))
            container_rect = container_surf.get_rect(midtop=(window_config.WIDTH / 2 + 400, 150))

            style_color = WHITE
            style_width = 0

            if player.style_meter < 100:
                container_surf.fill(WHITE)
                style_color = GREEN
                style_width = container_width * (player.style_meter / 100)

            elif player.style_meter < 300:
                container_surf.fill(GREEN)
                style_color = YELLOW
                style_width = container_width * ((player.style_meter - 100) / 200)

            else:
                container_surf.fill(YELLOW)
                style_color = RED
                style_width = container_width * ((player.style_meter - 300) / 300)

            pygame.draw.rect(container_surf, style_color, (0, 0, style_width, container_height))
            pygame.draw.rect(container_surf, GRAY, container_surf.get_rect(), 2)
            screen.blit(container_surf, container_rect)

        def display_player_health(screen):
            container_width, container_height = 300, 50
            container_surf = pygame.Surface((container_width, container_height))
            container_rect = container_surf.get_rect(midtop=(window_config.WIDTH / 2 - 400, 150))

            pygame.draw.rect(container_surf, RED, (0, 0, (container_width * (player.health / 100)), container_height))
            pygame.draw.rect(container_surf, GRAY, container_surf.get_rect(), 2)
            screen.blit(container_surf, container_rect)

        time.sleep(0.4)
        while running:
            window_config.CLOCK.tick(window_config.FPS)

            ret, frame = video.read()
            if not ret:
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Loop the video
                continue

            # Convert and display video frame
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type in event_triggers:
                    side_to_spawn = Fruit.sides_to_spawn[randint(0, 1)]
                    belong_to_sprite = left_fruits_sprites if side_to_spawn == 'Left' else right_fruits_sprites

                    timestamp = event_triggers[event.type]
                    fruits_dict = ghost_town.song[timestamp]

                    Fruit(
                        (all_sprites, belong_to_sprite),
                        side_to_spawn=side_to_spawn,
                        is_long=fruits_dict['is_long'],
                        health=fruits_dict['health'],
                        current_level=current_level,
                        perfect_overlay_left=perfect_overlay_left,
                        perfect_overlay_right=perfect_overlay_right,
                        asset_loader=asset_loader,
                        all_sprites=all_sprites,
                    )

                elif event.type in increase_speed_events:
                    current_level += 1
                    print(f'Level {current_level}')

                elif event.type in shake_camera_events:
                    camera.zoom_scale = (1 + ((current_level - 1) / 100))
                    camera.pulse_strength = current_level
                    camera.pulse_duration = 4
                    camera.value_to_decrement = (camera.zoom_scale - 1) / camera.pulse_duration
                    camera.frame_count = 0

            camera.internal_surface.blit(frame, (0, 0))
            all_sprites.draw(camera.internal_surface)

            display_score(camera.internal_surface)
            display_style_meter(camera.internal_surface)
            display_player_health(camera.internal_surface)

            camera.pulse()

            scaled_surface = pygame.transform.scale(camera.internal_surface,
                                                    camera.internal_surface_size_vector * camera.zoom_scale)
            scaled_rect = scaled_surface.get_rect(center=(window_config.WIDTH / 2, window_config.HEIGHT / 2))

            all_sprites.update(perfect_overlay_left, perfect_overlay_right)
            window_config.screen.blit(scaled_surface, scaled_rect)

            pygame.display.update()

        pygame.quit()

    @staticmethod
    def blit_screen(camera, align_with_player=False):
        if align_with_player:
            scaled_surface = pygame.transform.scale(camera.internal_surface,
                                                    camera.internal_surface_size_vector * camera.zoom_scale)
            scaled_rect = scaled_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 350))

        else:
            scaled_surface = pygame.transform.scale(camera.internal_surface,
                                                    camera.internal_surface_size_vector * camera.zoom_scale)
            scaled_rect = scaled_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))

        screen.blit(scaled_surface, scaled_rect)


if __name__ == '__main__':
    game = Game()
