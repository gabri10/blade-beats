import random
from random import randint

import pygame
import Config.window_config as window_config
from Config.camera import Camera
from Config.colors import *
from Sprites.pulsing_ring import PulsingRing

from Sprites.text_feedback import TextFeedback
from Sprites.flame_trailing import FlameTrailling


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups, all_sprites, perfect_overlay_left, perfect_overlay_right, good_overlay_left,
                 good_overlay_right, left_fruit_sprites,
                 right_fruit_sprites, asset_loader, game_panel):
        super().__init__(*groups)

        self.asset_loader = asset_loader
        self.image = asset_loader.assets['player']['idle'][0]
        self.game_panel = game_panel

        # Scale the image to match the rect size
        self.rect = self.image.get_rect(center=(window_config.WIDTH / 2, window_config.HEIGHT - 100))
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        self.hitbox = pygame.Rect(self.rect.left + 285, self.rect.top + 220, self.rect.width - 550, self.rect.height - 430)

        self.all_sprites = all_sprites

        self.perfect_overlay_left = perfect_overlay_left
        self.perfect_overlay_right = perfect_overlay_right

        self.good_overlay_left = good_overlay_left
        self.good_overlay_right = good_overlay_right

        self.left_fruit_sprites = left_fruit_sprites
        self.right_fruit_sprites = right_fruit_sprites

        self.margin_of_error = 0
        self.missed_counter = 0

        self.style_meter = 0
        self.score = 0
        self.perfects = 0
        self.goods = 0
        self.misses = 0
        self.style_meter_peak = 0
        self.health = 100

        self.is_hitting_long_fruit = False

        self.reaction_gap = 50

        self.cooldown_left = 10
        self.frames_after_killing_fruit_left = 0

        self.cooldown_right = 10
        self.frames_after_killing_fruit_right = 0

        self.animation_index = 0
        self.last_update_time = pygame.time.get_ticks()
        self.animation_speed = 200
        self.animation_on_side = None
        self.is_executing_animation = None
        self.last_executed_animation = None

        self.offset = 0

        self.is_player_dead = False

    def idle_animation(self):
        self.animation_speed = 200
        current_time = pygame.time.get_ticks()

        # If enough time has passed, update the animation
        if current_time - self.last_update_time > self.animation_speed:
            self.animation_index += 1
            self.image = self.asset_loader.assets['player']['idle'][self.animation_index % 4]
            self.last_update_time = current_time  # Update the last update time to the current time

    def death_animation(self):
        self.animation_speed = 200
        if self.is_executing_animation != 'Death':
            self.animation_index = 0
        self.is_executing_animation = 'Death'
        current_time = pygame.time.get_ticks()
        self.image = self.image
        if current_time - self.last_update_time > self.animation_speed:
            if self.animation_index >= len(self.asset_loader.assets['player']['death']):
                self.animation_index = 0
                self.is_executing_animation = None
                self.last_executed_animation = 'Death'
            else:
                # Get the next image in the animation
                original_image = self.asset_loader.assets['player']['death'][
                    self.animation_index % len(self.asset_loader.assets['player']['death'])]

                # Flip the image horizontally to make it go to the left
                self.image = original_image if self.animation_on_side == 'Right' else pygame.transform.flip(
                    original_image, True, False)

                self.last_update_time = current_time
                self.animation_index += 1

    def take_hit_animation(self):
        self.animation_speed = 50
        if self.is_executing_animation != 'Take hit':
            self.animation_index = 0
        self.is_executing_animation = 'Take hit'
        current_time = pygame.time.get_ticks()
        self.image = self.image
        if current_time - self.last_update_time > self.animation_speed:
            if self.animation_index >= len(self.asset_loader.assets['player']['take_hit']):
                self.animation_index = 0
                self.is_executing_animation = None
                self.last_executed_animation = 'Take hit'
            else:
                # Get the next image in the animation
                original_image = self.asset_loader.assets['player']['take_hit'][
                    self.animation_index % len(self.asset_loader.assets['player']['take_hit'])]

                # Flip the image horizontally to make it go to the left
                self.image = original_image if self.animation_on_side == 'Right' else pygame.transform.flip(
                    original_image, True, False)

                self.last_update_time = current_time
                self.animation_index += 1

    def attack_1_animation(self):
        self.animation_speed = 5
        direction = 1 if self.animation_on_side == 'Right' else -1
        original_position = (window_config.WIDTH / 2, self.rect.center[1])

        if self.is_executing_animation != 'Attack 1':
            self.animation_index = 0

            self.offset = 50 * direction
            self.rect.center = (original_position[0] + self.offset, original_position[1])

            if self.style_meter > 300:
                FlameTrailling(self.all_sprites, asset_loader=self.asset_loader, position=self.rect.center,
                               hit_side=self.animation_on_side, attack_axis='horizontal')
        else:
            # Gradually reduce the offset towards zero
            self.offset *= 0.9  # Reduce by 10% each frame for smooth deceleration

            # Update the position based on the reduced offset
            self.rect.center = (original_position[0] + self.offset, original_position[1])

            # Stop movement when close enough to center
            if abs(self.offset) < 1:
                self.rect.center = original_position  # Snap to the exact center
                self.offset = 0  # Ensure it stops moving

        self.is_executing_animation = 'Attack 1'
        current_time = pygame.time.get_ticks()

        # If enough time has passed, update the animation
        if current_time - self.last_update_time > self.animation_speed:
            if self.animation_index >= len(self.asset_loader.assets['player']['attack_1']):
                self.animation_index = 0
                self.is_executing_animation = None
                self.last_executed_animation = 'Attack 1'
            else:
                # Get the next image in the animation
                original_image = self.asset_loader.assets['player']['attack_1'][
                    self.animation_index % len(self.asset_loader.assets['player']['attack_1'])]

                # Flip the image horizontally to make it go to the left
                self.image = original_image if self.animation_on_side == 'Right' else pygame.transform.flip(
                    original_image, True, False)

                self.last_update_time = current_time
                self.animation_index += 1

    def attack_2_animation(self):
        self.animation_speed = 5

        direction = 1 if self.animation_on_side == 'Right' else -1
        original_position = (window_config.WIDTH / 2, self.rect.center[1])

        if self.is_executing_animation != 'Attack 2':
            self.animation_index = 0

            self.offset = 50 * direction
            self.rect.center = (original_position[0] + self.offset, original_position[1])

            if self.style_meter > 300:
                FlameTrailling(self.all_sprites, asset_loader=self.asset_loader, position=self.rect.center,
                               hit_side=self.animation_on_side, attack_axis='vertical')

        else:
            # Gradually reduce the offset towards zero
            self.offset *= 0.9  # Reduce by 10% each frame for smooth deceleration

            # Update the position based on the reduced offset
            self.rect.center = (original_position[0] + self.offset, original_position[1])

            # Stop movement when close enough to center
            if abs(self.offset) < 1:
                self.rect.center = original_position  # Snap to the exact center
                self.offset = 0  # Ensure it stops moving

        self.is_executing_animation = 'Attack 2'
        current_time = pygame.time.get_ticks()

        # If enough time has passed, update the animation
        if current_time - self.last_update_time > self.animation_speed:
            if self.animation_index >= len(self.asset_loader.assets['player']['attack_2']):
                self.animation_index = 0
                self.is_executing_animation = None
                self.last_executed_animation = 'Attack 2'
            else:
                # Get the next image in the animation
                original_image = self.asset_loader.assets['player']['attack_2'][
                    self.animation_index % len(self.asset_loader.assets['player']['attack_2'])]

                # Flip the image horizontally to make it go to the left
                self.image = original_image if self.animation_on_side == 'Right' else pygame.transform.flip(
                    original_image, True, False)

                # Update the last update time and increment the animation index
                self.last_update_time = current_time
                self.animation_index += 1

    def update(self, *args, **kwargs):
        Camera.camera_offset = [0, 0]

        if self.last_executed_animation != 'Death':
            if self.is_executing_animation == 'Attack 1':
                self.attack_1_animation()

            elif self.is_executing_animation == 'Attack 2':
                self.attack_2_animation()

            elif self.is_executing_animation == 'Take hit':
                self.take_hit_animation()
            elif self.is_executing_animation == 'Death':
                self.death_animation()
            else:
                self.idle_animation()

        if self.is_player_dead: return

        self.perfect_overlay_left.deactivate()
        self.perfect_overlay_right.deactivate()

        perfect_left_fruit_collisions = pygame.sprite.spritecollide(self.perfect_overlay_left,
                                                                    self.left_fruit_sprites, False)
        perfect_right_fruit_collisions = pygame.sprite.spritecollide(self.perfect_overlay_right,
                                                                     self.right_fruit_sprites,
                                                                     False)

        good_left_fruit_collisions = pygame.sprite.spritecollide(self.good_overlay_left, self.left_fruit_sprites,
                                                                 False)
        good_right_fruit_collisions = pygame.sprite.spritecollide(self.good_overlay_right, self.right_fruit_sprites,
                                                                  False)

        left_fruit = perfect_left_fruit_collisions[0] if perfect_left_fruit_collisions else \
            good_left_fruit_collisions[0] if good_left_fruit_collisions else None
        right_fruit = perfect_right_fruit_collisions[0] if perfect_right_fruit_collisions else \
            good_right_fruit_collisions[0] if good_right_fruit_collisions else None

        self.input(0, left_fruit, area_hit=2 if perfect_left_fruit_collisions else 1)
        self.input(2, right_fruit, area_hit=2 if perfect_right_fruit_collisions else 1)

        self.frames_after_killing_fruit_left += 1
        self.frames_after_killing_fruit_right += 1
        self.player_hit_check()

    def input(self, side, fruit, area_hit):
        mouse_inputs = pygame.mouse.get_pressed()
        is_pressing_side = mouse_inputs[side]

        if fruit is not None:
            fruit.move()

        if side == 0:
            cooldown = self.cooldown_left
            frames_after_killing_fruit = self.frames_after_killing_fruit_left
        else:
            cooldown = self.cooldown_right
            frames_after_killing_fruit = self.frames_after_killing_fruit_right

        if is_pressing_side and (cooldown < frames_after_killing_fruit):
            self.animation_on_side = 'Right' if side == 2 else 'Left'

            if self.last_executed_animation is None:
                self.attack_1_animation() if random.randint(0, 1) == 0 else self.attack_2_animation()
            elif self.last_executed_animation == 'Attack 1':
                self.attack_2_animation()
            else:
                self.attack_1_animation()

            if side == 0:
                self.perfect_overlay_left.activate()
            else:
                self.perfect_overlay_right.activate()

            if fruit is not None:
                self.hit_fruit(fruit, area_hit, side)
            else:
                self.missed()

            return pygame.time.get_ticks()

    def hit_fruit(self, fruit, area_hit, side):
        slice_side = 'vertical' if self.is_executing_animation == 'Attack 2' else 'horizontal'
        self.missed_counter = 0
        fruit.hit(slice_side)
        self.score += (1 + (self.style_meter * 0.1)) * area_hit

        if fruit.health < 1:
            fruit.kill()
            # PulsingRing(self.all_sprites, reference_point=self.perfect_overlay_left, max_radius=1000, pulse_speed=10, thickness=3, permanent=False)
            if side == 0:
                self.frames_after_killing_fruit_left = 0
            else:
                self.frames_after_killing_fruit_right = 0
            self.style_meter += 10

            if self.style_meter > self.style_meter_peak:
                self.style_meter_peak = self.style_meter

            self.is_hitting_long_fruit = False

            if area_hit == 2:
                TextFeedback(self.all_sprites, position=fruit.rect.midtop, text='Perfeito!', color=GOLD)
                self.perfects += 1
            else:
                TextFeedback(self.all_sprites, position=fruit.rect.midtop, text='Boa!', color=GREEN)
                self.goods += 1
        else:
            self.is_hitting_long_fruit = True

    def missed(self):
        if self.missed_counter < self.margin_of_error:
            self.missed_counter += 1
        else:
            self.style_meter = 0
            self.missed_counter = 0
            self.misses += 1
            TextFeedback(self.all_sprites, position=self.rect.midtop, text='Errou', color=RED)
            self.health -= 1
            if self.health < 1:
                sound = self.asset_loader.assets["sounds"]["player_hit"][randint(0, 6)]
                sound.play()
                self.is_player_dead = True
                self.death_animation()

    def player_hit_check(self):
        # Use the player's custom hitbox for collisions instead of the full rect
        left_collisions = pygame.sprite.spritecollide(self, self.left_fruit_sprites, False)
        right_collisions = pygame.sprite.spritecollide(self, self.right_fruit_sprites, False)

        # Check if any fruit collided with the player's hitbox
        colliding_fruit_with_player = None

        # Check collisions on the left side
        for fruit in left_collisions:
            if self.hitbox.colliderect(fruit.rect):  # Use hitbox for the collision check
                colliding_fruit_with_player = fruit
                break  # Stop checking once a collision is found

        # If no collision found on the left, check the right side
        if colliding_fruit_with_player is None:
            for fruit in right_collisions:
                if self.hitbox.colliderect(fruit.rect):  # Use hitbox for the collision check
                    colliding_fruit_with_player = fruit
                    break  # Stop checking once a collision is found

        # Handle the collision if any fruit collided
        if colliding_fruit_with_player:
            self.animation_on_side = 'Right' if colliding_fruit_with_player.movement_direction == 1 else 'Left'
            self.take_hit_animation()
            sound = self.asset_loader.assets["sounds"]["player_hit"][randint(0, 6)]
            sound.play()
            TextFeedback(self.all_sprites, position=self.rect.midtop, text='Acertou jogador', color=RED)
            self.health -= 1
            if self.health < 1:
                self.is_player_dead = True
                self.death_animation()
            if colliding_fruit_with_player.is_last_fruit:
                self.game_panel.game_ended = True
            colliding_fruit_with_player.kill()
            if colliding_fruit_with_player.health < 1:
                colliding_fruit_with_player.kill()
            self.style_meter = 0