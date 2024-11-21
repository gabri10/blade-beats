import pygame
import Config.window_config as window_config


class Camera:
    def __init__(self):
        self.zoom_scale = 1.0
        self.pulse_duration = 1
        self.frame_count = 0
        self.value_to_decrement = 0
        self.is_pulsing = False

        self.start_zoom = 1.0
        self.target_zoom = 1.0

        self.internal_surface_size = (window_config.WIDTH, window_config.HEIGHT)
        self.internal_surface = pygame.Surface(self.internal_surface_size, pygame.SRCALPHA)
        self.internal_rectangle = self.internal_surface.get_rect(
            center=(window_config.WIDTH / 2, window_config.HEIGHT / 2))
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surface_size)

    def ease_in_out_quad(self, t):
        if t < 0.5:
            return 2 * t * t
        return 1 - (-2 * t + 2) ** 2 / 2

    def pulse(self):
        if not self.is_pulsing:
            return

        if self.frame_count >= self.pulse_duration:
            self.zoom_scale = 1.0
            self.is_pulsing = False
            self.frame_count = 0
        else:
            progress = self.frame_count / self.pulse_duration
            eased_progress = self.ease_in_out_quad(progress)
            self.zoom_scale = self.start_zoom + (self.target_zoom - self.start_zoom) * eased_progress
            self.frame_count += 1

    def setup_pulse(self, first_zoom, duration):
        self.start_zoom = first_zoom
        self.target_zoom = 1.0
        self.pulse_duration = max(1, duration)
        self.frame_count = 0
        self.is_pulsing = True
