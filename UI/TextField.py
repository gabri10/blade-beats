import pygame as pg
from Config.window_config import *

COLOR_INACTIVE = pg.Color(GRAY)
COLOR_ACTIVE = pg.Color(WHITE)
font = pg.font.Font(FONT, 24)
BORDER_WIDTH = 2

class TextField:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.border_color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False
        self.hovered = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # Toggle active state when clicked
            self.active = self.rect.collidepoint(event.pos)
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
            self.border_color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        elif event.type == pg.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
            self.border_color = COLOR_ACTIVE if self.hovered or self.active else COLOR_INACTIVE
        elif event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = font.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Draw the border around the text field
        pg.draw.rect(screen, self.border_color, self.rect, BORDER_WIDTH)
        # Draw the text inside the text field
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))