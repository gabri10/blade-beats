import pygame
from Config.window_config import *


class Rankings(pygame.sprite.Sprite):

    def __init__(self, *groups, asset_loader, player):
        super().__init__(*groups)
        self.player = player
        self.asset_loader = asset_loader
        self.image = pygame.Surface((0, 0), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topright=(WIDTH - 50, 50))

    def update(self, *args, **kwargs):
        old_image = self.image
        if self.player.style_meter == 0:
            self.image = pygame.Surface((0, 0), pygame.SRCALPHA)
            return

        if self.player.style_meter >= 1000:
            index = 6
        elif self.player.style_meter >= 700:
            index = 5
        elif self.player.style_meter >= 450:
            index = 4
        elif self.player.style_meter >= 250:
            index = 3
        elif self.player.style_meter >= 100:
            index = 2
        elif self.player.style_meter >= 50:
            index = 1
        else:
            index = 0


        self.image = self.asset_loader.assets['rankings'][index]
        self.rect = self.image.get_rect(topright=(WIDTH - 50, 50))

        if old_image != self.image:
            audio = self.asset_loader.assets['sounds']['rankings'][index]
            audio.play()
