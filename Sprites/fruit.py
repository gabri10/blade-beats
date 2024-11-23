from random import randint

import pygame.sprite

import Config.window_config as window_config
from Sprites.fruit_death import FruitDeath
from Sprites.perfect_overlay import PerfectOverlay

from Config.colors import *


class Fruit(pygame.sprite.Sprite):
    sides_to_spawn = ['Left', 'Right']

    slash_audio_cooldown = 10
    slash_audio_counter = 0

    def __init__(self, *groups, all_sprites, side_to_spawn, is_long, health=1, current_level, perfect_overlay_left, perfect_overlay_right, asset_loader, is_last_fruit=False, game_panel):
        super().__init__(*groups)

        self.game_panel = game_panel
        self.is_last_fruit = is_last_fruit
        self.asset_loader = asset_loader
        self.all_sprites = all_sprites

        self.health = health

        self.distance_to_travel = ((window_config.WIDTH / 2) - PerfectOverlay.width / 2)
        self.distance_to_travel *= (1 + (current_level * 0.25))

        self.side_to_spawn = side_to_spawn

        self.speed = self.distance_to_travel / 60
        self.length = 10

        self.gap = 50

        self.is_long = is_long

        self.perfect_overlay_left = perfect_overlay_left
        self.perfect_overlay_right = perfect_overlay_right

        self.squish = 0.8

        if self.is_long:
            self.long_fruit_dict = {
                1: 17,
                2: 18,
                3: 19,
                4: 26,
                5: 55,
                6: 56,
                7: 57
            }
            self.sprite_index = randint(1, 7)
            self.sprite_index = self.long_fruit_dict[self.sprite_index]
            self.set_long_image()
        else:
            self.sprite_index = randint(1, 227)
            self.image = asset_loader.assets['fruits'][self.sprite_index]

        if side_to_spawn == 'Left':
            self.movement_direction = -1
            self.rect = self.image.get_rect(midright=(
                ((window_config.WIDTH / 2) - PerfectOverlay.width / 2) - self.distance_to_travel - self.gap,
                window_config.HEIGHT - 100))
        else:
            self.movement_direction = 1
            self.rect = self.image.get_rect(midleft=(
                ((window_config.WIDTH / 2) + PerfectOverlay.width / 2) + self.distance_to_travel + self.gap,
                window_config.HEIGHT - 100))

    def update(self, current_level, *args, **kwargs):
        self.rect.x -= self.speed * self.movement_direction

    def stop(self):
        self.movement_direction = 0

    def move(self):
        self.movement_direction = -1 if self.side_to_spawn == 'Left' else 1

    def hit(self, slice_side='horizontal'):
        self.health -= 1
        self.stop()
        self.length = self.health * self.speed
        should_downscale = self.health > 1

        if Fruit.slash_audio_cooldown <= Fruit.slash_audio_counter:
            sound = self.asset_loader.assets['sounds']['fruit_slashed'][
                randint(0, len(self.asset_loader.assets['sounds']['fruit_slashed']) - 1)]
            sound.play()
            Fruit.slash_audio_counter = 0

        FruitDeath(self.all_sprites, asset_loader=self.asset_loader, sliced_fruit=self, slice_side=slice_side, index=0, should_downscale=should_downscale)
        FruitDeath(self.all_sprites, asset_loader=self.asset_loader, sliced_fruit=self, slice_side=slice_side, index=1, should_downscale=should_downscale)

        if self.health < 1:
            if self.is_last_fruit:
                self.game_panel.activate_slow_motion()

        if self.health > 1:
            self.set_long_image()

        if self.side_to_spawn == 'Left':
            self.rect = self.image.get_rect(midright=(self.perfect_overlay_left.rect.midright))
        else:
            self.rect = self.image.get_rect(midleft=(self.perfect_overlay_right.rect.midleft))

    def set_long_image(self):
        # Calculate the desired length based on health and speed
        self.length = self.health * self.speed * self.squish

        # Load the start, middle, and end images
        start_image = self.asset_loader.assets['long_fruits'][self.sprite_index]['start']
        middle_image = self.asset_loader.assets['long_fruits'][self.sprite_index]['middle']
        end_image = self.asset_loader.assets['long_fruits'][self.sprite_index]['end']

        # Calculate the width of the start, middle, and end images
        start_width = start_image.get_width()
        middle_width = middle_image.get_width()
        end_width = end_image.get_width()

        # Calculate the height (assuming all images have the same height)
        image_height = start_image.get_height()

        # Create the surface with the calculated length
        self.image = pygame.Surface((self.length * self.squish, image_height), pygame.SRCALPHA)

        # Calculate how many middle images we need to fill the space
        number_of_middles = int((self.length - (start_width + end_width)) / middle_width)

        # Start blitting the images into the blank surface
        self.image.blit(start_image, (0, 0))  # Place the start image at the beginning
        x_offset = start_width  # Update the offset after placing the start image

        # Add middle images until the width is greater than or equal to the desired length
        for i in range(0, number_of_middles):
            self.image.blit(middle_image, (x_offset, 0))  # Place the middle image
            x_offset += middle_width * self.squish  # Update the offset

        # After filling with middle images, place the end image at the end
        self.image.blit(end_image, (x_offset, 0))  # Place the end image

        # Add a border around the final image
        border_thickness = 2  # Set the thickness of the border
        border_color = (255, 0, 0)  # Red color for the border