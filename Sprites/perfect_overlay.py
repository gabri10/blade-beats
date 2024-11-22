import pygame
from Config.colors import *
from Sprites.pulsing_ring import PulsingRing


class PerfectOverlay(pygame.sprite.Sprite):
    width = 100
    height = 100

    def __init__(self, *groups, position, all_sprites):
        super().__init__(*groups)

        self.all_sprites = all_sprites

        self.image = pygame.Surface((PerfectOverlay.width, PerfectOverlay.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=position)

        self.deactivate()
        self.is_active = False

    def activate(self):
        self.image.fill(YELLOW)
        self.draw_border()
        self.is_active = True
        PulsingRing(self.all_sprites, max_radius=500, pulse_speed=10, reference_point=self, thickness=5, permanent=False)

    def deactivate(self):
        self.image.fill(TRANSPARENT)
        self.draw_border()
        self.is_active = False
    def draw_border(self):
        pygame.draw.rect(
            self.image,
            GRAY,
            self.image.get_rect(),
            4,
        )
