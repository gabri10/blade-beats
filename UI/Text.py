import pygame
from Config.window_config import *


class Text:
    def __init__(self, msg, position, color=(100, 100, 100), font=None, font_size=15, centered=False):
        self.position = position
        self.font = pygame.font.Font(FONT, font_size)
        self.msg = msg
        self.color = color
        self.text_surface = self.font.render(msg, True, color)
        self.centered = centered
        self.pos = position

        if len(color) == 4:
            self.text_surface.set_alpha(color[3])

        if centered:
            self.position = self.text_surface.get_rect(center=position)

    def draw(self, screen):
        self.text_surface = self.font.render(self.msg, True, self.color)
        if len(self.color) == 4:
            self.text_surface.set_alpha(self.color[3])

        if self.centered:
            self.position = self.text_surface.get_rect(center=self.pos)
        screen.blit(self.text_surface, self.position)
