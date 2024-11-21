import pygame

from Config import window_config
from Sprites.fruit_death import FruitDeath
from Sprites.perfect_overlay import PerfectOverlay


class CheckpointStar(pygame.sprite.Sprite):
    def __init__(self, *groups, all_sprites, side_to_spawn, current_level, asset_loader, game_panel, is_last_fruit):
        super().__init__(*groups)

        self.game_panel = game_panel
        self.asset_loader = asset_loader
        self.all_sprites = all_sprites

        self.health = 1
        self.is_last_fruit = is_last_fruit

        self.distance_to_travel = ((window_config.WIDTH / 2) - PerfectOverlay.width / 2)
        self.distance_to_travel *= (1 + (current_level * 0.25))

        self.side_to_spawn = side_to_spawn

        self.speed = self.distance_to_travel / 60
        self.length = 10

        self.squish = 0.8

        self.sprite_index = 228
        self.image = asset_loader.assets['star'][0]

        self.sound = self.asset_loader.assets['sounds']['checkpoint']

        if side_to_spawn == 'Left':
            self.movement_direction = -1
            self.rect = self.image.get_rect(midright=(
                ((window_config.WIDTH / 2) - PerfectOverlay.width / 2) - self.distance_to_travel,
                window_config.HEIGHT - 100))
        else:
            self.movement_direction = 1
            self.rect = self.image.get_rect(midleft=(
                ((window_config.WIDTH / 2) + PerfectOverlay.width / 2) + self.distance_to_travel,
                window_config.HEIGHT - 100))

    def update(self, current_level, *args, **kwargs):
        self.rect.x -= self.speed * self.movement_direction

    def stop(self):
        self.movement_direction = 0

    def move(self):
        self.movement_direction = -1 if self.side_to_spawn == 'Left' else 1

    def hit(self, slice_side='horizontal'):
        self.health -= 1
        self.kill()
        self.sound.play()
        FruitDeath(self.all_sprites, asset_loader=self.asset_loader, sliced_fruit=self, slice_side=slice_side,
                   index=0, should_downscale=True)
        FruitDeath(self.all_sprites, asset_loader=self.asset_loader, sliced_fruit=self, slice_side=slice_side,
                   index=1, should_downscale=True)
