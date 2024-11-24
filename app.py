import pygame

pygame.init()
pygame.mixer.init()


import time
from random import randint
import cv2

from Config.window_config import *
from Config.colors import *
from Config.camera import Camera

from Sprites.player import Player
from Sprites.fruit import Fruit

from Sprites.perfect_overlay import PerfectOverlay
from Sprites.good_overlay import GoodOverlay


class Game:
    def __init__(self):
        camera = Camera()

        from UI.Menus.boot import Boot
        from UI.Menus.login import Login
        from UI.Menus.main import Main
        from UI.Menus.play import Play

        boot = Boot(camera=camera)
        asset_loader = boot.run()

        login = Login(camera=camera)
        main = Main(camera=camera, player=None, asset_loader=asset_loader)
        play = Play(camera=camera, song=None, asset_loader=asset_loader, player_info=None)

        running = True
        self.next_action = 'Login'

        while running:
            CLOCK.tick(FPS)
            match self.next_action:
                case 'Login':
                    response = login.run()
                    if response is not None:
                        main.player = response
                        play.player_info = response
                        self.next_action = 'Main'
                case 'Main':
                    response = main.run()
                    if response is not None:
                        play.song = response
                        self.next_action = 'Play'
                case 'Play':
                    self.next_action = play.run()

    @staticmethod
    def blit_screen(camera, align_with_player=False):
        if align_with_player:
            scaled_surface = pygame.transform.scale(camera.internal_surface,
                                                    camera.internal_surface_size_vector * camera.zoom_scale)
            scaled_rect = scaled_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 350))

        else:
            scaled_surface = pygame.transform.scale(camera.internal_surface,
                                                    camera.internal_surface_size_vector * camera.zoom_scale)
            scaled_rect = scaled_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))

        screen.blit(scaled_surface, scaled_rect)


if __name__ == '__main__':
    game = Game()
