import pygame as pg
from Config.window_config import *

from UI.Button import Button


class SongCard:
    def __init__(self, position, song_name, creator, album_image_path, songs_fps):
        self.width = int(WIDTH * 0.6)
        self.height = 120

        self.songs_fps = songs_fps

        self.x = position[0]
        self.y = position[1]

        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

        self.background_color = pg.Color('darkgray')
        self.border_color = pg.Color('white')
        self.text_color = pg.Color('white')
        self.hover_color = pg.Color('gray')

        self.font = pg.font.Font(FONT, 24)
        self.song_name = song_name
        self.creator = creator

        self.album_image = pg.image.load(album_image_path)
        self.album_image = pg.transform.scale(self.album_image, (100, 100))  # Fixed size for album image

        self.play_button = Button(position=(self.width - 60, self.y + self.height - 35), size=(200, 50), color=GRAY, text="Jogar")

        self.hovered = False
        self.button_pressed = False

    def handle_event(self, event):
        if self.button_pressed:
            return 'Go to game'

        if event.type == pg.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.play_button.rect.collidepoint(event.pos):
                return 'Go to game'

            if self.hovered:
                return 'Update UI elements'


    def draw(self, screen):

        color = self.hover_color if self.hovered else self.background_color
        pg.draw.rect(screen, color, self.rect)
        pg.draw.rect(screen, self.border_color, self.rect, 2)  # Border

        image_padding = 10
        screen.blit(self.album_image,
                    (self.x + image_padding,
                     self.y + (self.height - self.album_image.get_height()) // 2))

        text_x = self.x + self.album_image.get_width() + 20

        song_surface = self.font.render(self.song_name, True, self.text_color)
        screen.blit(song_surface,
                    (text_x,
                     self.y + self.height // 4 - song_surface.get_height() // 2))

        creator_surface = self.font.render(self.creator, True, self.text_color)
        screen.blit(creator_surface, (text_x, self.y + 3 * self.height // 4 - creator_surface.get_height() // 2))

        self.play_button.draw(screen)
