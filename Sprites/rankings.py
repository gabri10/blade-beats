import random
import math
from Config.window_config import *


class Rankings(pygame.sprite.Sprite):
    def __init__(self, *groups, asset_loader, player):
        super().__init__(*groups)
        self.player = player
        self.asset_loader = asset_loader
        self.image = pygame.Surface((0, 0), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topright=(WIDTH - 50, 50))

        self.current_index = None

        self.play_intro = False
        self.intro_index = 0

        self.original_width = 0
        self.original_height = 0
        self.original_image = None

        self.initial_upscale = 3
        self.new_scale = 0
        self.downscale_time = 12
        self.alpha = 0

        self.slam_time = self.downscale_time + 10

        # New pulse animation variables
        self.pulse_timer = 0
        self.pulse_speed = 0.1  # Base speed of the pulse
        self.base_pulse_intensity = 0.02  # Base intensity of the pulse
        self.pulse_scale = 1.0

    def update(self, *args, **kwargs):
        if self.play_intro:
            self.animate_intro()
        else:
            self.animate_pulse()  # Apply pulse animation when not in intro

        if self.player.style_meter == 0:
            self.image = pygame.Surface((0, 0), pygame.SRCALPHA)
            self.current_index = None
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

        if self.current_index != index:
            self.current_index = index
            self.image = self.asset_loader.assets['rankings'][index]
            self.rect = self.image.get_rect(topright=(WIDTH - 50, 50))

            self.setup_animation_intro()
            audio = self.asset_loader.assets['sounds']['rankings'][index]
            audio.play()

    def animate_intro(self):
        self.image = self.original_image

        if self.intro_index < self.downscale_time:
            self.new_scale -= (self.initial_upscale - 1) / self.downscale_time

            width = self.original_width * self.new_scale
            height = self.original_height * self.new_scale

            self.alpha = min(255, int((self.intro_index / self.downscale_time) * 255))

            self.image = pygame.transform.scale(self.image, (width, height))
            self.image.set_alpha(self.alpha)

        elif self.intro_index < self.slam_time:
            offset_x = random.randint(-10, 10)
            offset_y = random.randint(-10, 10)

            bounce_scale = 1 + (0.05 if self.intro_index % 2 == 0 else -0.05)

            self.image = pygame.transform.scale(
                self.image,
                (int(self.image.get_width() * bounce_scale), int(self.image.get_height() * bounce_scale))
            )
            self.rect.x += offset_x
            self.rect.y += offset_y
        else:
            self.play_intro = False  # End intro animation

        self.intro_index += 1

    def animate_pulse(self):
        if not self.original_image or self.play_intro:
            return

        # Increase pulse intensity based on current_index
        intensity_multiplier = 1 + (self.current_index or 0) * 1
        pulse_intensity = self.base_pulse_intensity * intensity_multiplier

        # Calculate pulse scale using sine wave
        self.pulse_timer += self.pulse_speed
        self.pulse_scale = 1 + pulse_intensity * math.sin(self.pulse_timer)

        # Apply pulse scale to image
        scaled_width = int(self.original_width * self.pulse_scale)
        scaled_height = int(self.original_height * self.pulse_scale)

        self.image = pygame.transform.scale(self.original_image, (scaled_width, scaled_height))

        # Maintain position relative to top right corner
        self.rect = self.image.get_rect(topright=(WIDTH - 50, 50))

    def setup_animation_intro(self):
        self.original_width = self.image.get_width()
        self.original_height = self.image.get_height()
        self.original_image = self.image

        self.image = pygame.transform.scale(self.image, (
            self.image.get_width() * self.initial_upscale,
            self.image.get_height() * self.initial_upscale))

        self.new_scale = self.initial_upscale
        self.intro_index = 0
        self.play_intro = True
        self.pulse_scale = 1.0