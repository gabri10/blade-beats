import pygame.font

from Config.window_config import *
class Button:
    def __init__(self, position, size, color=(100, 100, 100), hover_color=None, on_click=None, text='', font_size=16, font_color=BLACK):
        self.color = color
        self.size = size
        self.on_click = on_click
        self.surface = pygame.Surface(size)
        self.rect = self.surface.get_rect(center=position)

        if hover_color:
            self.hover_color = hover_color
        else:
            self.hover_color = color

        if len(color) == 4:
            self.surface.set_alpha(color[3])

        self.font = pygame.font.Font(FONT, font_size)
        self.text = text
        self.font_color = font_color
        self.text_surface = self.font.render(self.text, True, self.font_color)
        self.text_rect = self.text_surface.get_rect(center=[wh // 2 for wh in self.size])

    def draw(self, screen):
        self.check_hover()
        self.surface.fill(self.current_color)
        self.surface.blit(self.text_surface, self.text_rect)
        screen.blit(self.surface, self.rect)

    def check_hover(self):
        self.current_color = self.color
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.current_color = self.hover_color

    def handle_click(self):
        if self.on_click:
            self.on_click()
