import pygame


class PulsingRing(pygame.sprite.Sprite):
    def __init__(self, *groups, max_radius, pulse_speed, thickness, reference_point, permanent=True):
        super().__init__(*groups)
        self.reference_point = reference_point
        self.permanent = permanent
        self.max_radius = max_radius  # The maximum radius for the pulse
        self.pulse_speed = pulse_speed  # Speed of the pulsing effect
        self.thickness = thickness  # Thickness of the ring border
        self.current_radius = 0  # Initial radius of the ring
        self.alpha = 255  # Initial opacity

        # Initialize the image surface
        self.image = pygame.Surface((self.max_radius * 2, self.max_radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=reference_point.rect.center)

    def update(self, *args, **kwargs):
        # Increment the radius
        self.current_radius += self.pulse_speed

        # Fade out as it expands
        self.alpha = max(0, 255 - int((self.current_radius / self.max_radius) * 255))
        if self.alpha == 0 and not self.permanent:
            self.kill()

        # Reset pulse if it exceeds max_radius
        if self.current_radius > self.max_radius:
            self.current_radius = 0  # Reset radius
            self.alpha = 255  # Reset opacity

        # Clear the surface
        self.image.fill((0, 0, 0, 0))

        # Draw the ring with the current radius, thickness, and alpha
        pulsing_color = (255, 255, 255, self.alpha)  # White with variable opacity
        pygame.draw.circle(self.image, pulsing_color, (self.max_radius, self.max_radius), int(self.current_radius),
                           self.thickness)

        # Update rect to keep it centered
        self.rect = self.image.get_rect(center=self.reference_point.rect.center)



"""
import pygame


class PulsingRing(pygame.sprite.Sprite):
    def __init__(self, *groups, max_radius, pulse_speed, thickness, reference_point, permanent=True):
        super().__init__(*groups)
        self.reference_point = reference_point
        self.permanent = permanent
        self.max_radius = max_radius  # The maximum radius for the pulse
        self.pulse_speed = pulse_speed  # Speed of the pulsing effect
        self.thickness = thickness  # Thickness of the ring border
        self.current_radius = 0  # Initial radius of the ring
        self.alpha = 255  # Initial opacity

        # Initialize the image surface
        self.image = pygame.Surface((self.max_radius, self.max_radius), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=reference_point.rect.center)

    def update(self, *args, **kwargs):
        # Increment the radius
        self.current_radius += self.pulse_speed

        # Fade out as it expands
        self.alpha = max(0, 255 - int((self.current_radius / self.max_radius) * 255))
        if self.alpha == 0 and not self.permanent:
            self.kill()

        # Reset pulse if it exceeds max_radius
        if self.current_radius > self.max_radius:
            self.current_radius = 0  # Reset radius
            self.alpha = 255  # Reset opacity

        # Clear the surface
        self.image.fill((0, 0, 0, 0))

        # Draw the ring with the current radius, thickness, and alpha
        pulsing_color = (255, 255, 255, self.alpha)  # White with variable opacity
        pygame.draw.circle(self.image, pulsing_color, (self.max_radius, self.max_radius), int(self.current_radius),
                           self.thickness)

        # Update rect to keep it centered
        self.rect = self.image.get_rect(center=self.reference_point.rect.center)
"""