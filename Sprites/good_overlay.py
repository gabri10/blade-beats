import pygame
from Config.colors import *


class GoodOverlay(pygame.sprite.Sprite):
    width = 100
    height = 100

    def __init__(self, *groups, position):
        super().__init__(*groups)

        self.image = pygame.Surface((GoodOverlay.width, GoodOverlay.height), pygame.SRCALPHA)
        self.image.fill(TRANSPARENT)

        self.rect = self.image.get_rect(center=position)