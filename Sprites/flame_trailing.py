from random import randint

import pygame.sprite


class FlameTrailling(pygame.sprite.Sprite):
    def __init__(self, *groups, asset_loader, position, hit_side, attack_axis):
        super().__init__(*groups)

        self.animation = [
            pygame.transform.flip(image, hit_side == 'Left', attack_axis == 'vertical')
            for image in asset_loader.assets['player']['trailing_slash']
        ]

        self.animation_index = 0

        # Set the initial image
        self.image = self.animation[self.animation_index]

        self.offset = 1 if hit_side == 'Right' else -1

        # Set the rectangle for positioning
        self.rect = self.image.get_rect(center=(position[0] + (100 * self.offset), position[1]))

    def update(self, *args, **kwargs):
        # Increment the animation index
        self.animation_index += 0.5

        # Check if the animation should end
        if self.animation_index >= len(self.animation):
            self.kill()
        else:
            # Update the image based on the animation index
            self.image = self.animation[int(self.animation_index)]
