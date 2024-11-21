import pygame
import random
from pygame import Surface
from typing import List, Tuple


class FruitDeath(pygame.sprite.Sprite):
    # Class-level constants to avoid recreating values
    GRAVITY = 0.5
    MAX_FRAMES = 60 * 1  # 5 seconds at 60 FPS
    ROTATION_SPEED = 6
    DOWNSCALE_VALUE = 0.3

    # Pre-calculate commonly used values
    @classmethod
    def precalculate_values(cls):
        cls.alpha_steps = [max(0, 255 - int(255 * (i / cls.MAX_FRAMES))) for i in range(cls.MAX_FRAMES + 1)]
        cls.scale_factors = [max(0.5, 1.0 - (i / cls.MAX_FRAMES)) for i in range(cls.MAX_FRAMES + 1)]
        cls.angles = [(i * cls.ROTATION_SPEED) % 360 for i in range(cls.MAX_FRAMES + 1)]

    def __init__(self, *groups, asset_loader, sliced_fruit, slice_side, index, should_downscale=False):
        super().__init__(*groups)
        sliced_fruit.move()

        self.original_image = \
        asset_loader.assets['sliced_fruits'][f'Fruit_{sliced_fruit.sprite_index + 1}'][slice_side][index]
        self.original_width = self.original_image.get_width()
        self.original_height = self.original_image.get_height()

        self._setup_initial_position(sliced_fruit, index)

        self.movement_direction = sliced_fruit.movement_direction
        self.speed = sliced_fruit.speed
        self.vertical_velocity = random.uniform(-5, -10)

        self.frames_alive = 0
        self.should_downscale = should_downscale

        self._update_image(0)

    def _setup_initial_position(self, sliced_fruit, index):
        self.rect = self.original_image.get_rect()
        if sliced_fruit.movement_direction == 1:  # Moving from left to right
            self.rect.midright = sliced_fruit.rect.midleft
        else:  # Moving from right to left
            self.rect.midleft = sliced_fruit.rect.midright

    def _update_image(self, frame):
        # Get pre-calculated values
        scale = self.scale_factors[frame]
        alpha = self.alpha_steps[frame]
        angle = self.angles[frame]

        # Calculate new size
        final_scale = scale * (self.DOWNSCALE_VALUE if self.should_downscale else 1.0)
        new_width = int(self.original_width * final_scale)
        new_height = int(self.original_height * final_scale)

        # Rotate and scale in one operation
        self.image = pygame.transform.rotozoom(self.original_image, angle, final_scale)

        # Set alpha
        self.image.set_alpha(alpha)

        # Update rect while maintaining center
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self, *args, **kwargs):
        self.frames_alive += 1
        if self.frames_alive >= self.MAX_FRAMES:
            self.kill()
            return

        # Update position
        self.vertical_velocity += self.GRAVITY
        self.rect.y += self.vertical_velocity
        self.rect.x -= self.speed * self.movement_direction

        # Update image state
        self._update_image(self.frames_alive)


# Initialize pre-calculated values
FruitDeath.precalculate_values()


