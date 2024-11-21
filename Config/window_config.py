import pygame
from Config.colors import *

WIDTH = 1280
HEIGHT = 720
FONT = 'Config/PixelatedFont.ttf'

FPS = 60

CLOCK = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(DARK_GRAY)
pygame.display.set_caption('Blade Beats')
