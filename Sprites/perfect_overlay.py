import pygame
from Config.colors import *


class PerfectOverlay(pygame.sprite.Sprite):
    width = 100
    height = 100

    def __init__(self, *groups, position, rings):
        super().__init__(*groups)

        self.rings = rings

        self.image = pygame.Surface((PerfectOverlay.width, PerfectOverlay.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=position)

        self.deactivate()

    def activate(self):
        self.image.fill(YELLOW)
        self.draw_border()

    def deactivate(self):
        self.image.fill(TRANSPARENT)
        self.draw_border()

    def draw_border(self):
        pygame.draw.rect(
            self.image,
            GRAY,
            self.image.get_rect(),
            4,
        )
