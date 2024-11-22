import pygame


class PulsingRing(pygame.sprite.Sprite):
    # Class-level cache for shared frames, keyed by unique parameters
    shared_cache = {}

    def __init__(self, *groups, max_radius, pulse_speed, thickness, reference_point, permanent=True, cache_frames=10):
        super().__init__(*groups)
        self.reference_point = reference_point
        self.permanent = permanent
        self.max_radius = max_radius
        self.pulse_speed = pulse_speed
        self.thickness = thickness
        self.cache_frames = cache_frames  # Number of frames to cache
        self.current_frame = 0

        # Use the unique key for this configuration to access shared cache
        cache_key = (self.max_radius, self.pulse_speed, self.thickness, self.cache_frames)

        # Retrieve cached frames if they exist, otherwise create and store them
        if cache_key not in PulsingRing.shared_cache:
            PulsingRing.shared_cache[cache_key] = self._create_cached_frames()

        self.cached_surfaces = PulsingRing.shared_cache[cache_key]

        # Set the initial image
        self.image = self.cached_surfaces[0]
        self.rect = self.image.get_rect(center=reference_point.rect.center)

    def _create_cached_frames(self):
        """Pre-renders and caches frames of the pulsing effect to avoid redundant calculations."""
        cached_surfaces = []
        for i in range(self.cache_frames):
            # Calculate radius and alpha for each frame
            radius = (i / self.cache_frames) * self.max_radius
            alpha = max(0, 255 - int((radius / self.max_radius) * 255))

            # Create a new surface for this frame
            frame_surface = pygame.Surface((self.max_radius * 2, self.max_radius * 2), pygame.SRCALPHA)
            pulsing_color = (255, 255, 255, alpha)
            pygame.draw.circle(frame_surface, pulsing_color, (self.max_radius, self.max_radius), int(radius),
                               self.thickness)
            cached_surfaces.append(frame_surface)

        return cached_surfaces

    def update(self, *args, **kwargs):
        # Cycle through cached frames
        self.image = self.cached_surfaces[self.current_frame]
        self.current_frame += 1

        # Reset or remove based on permanent flag
        if self.current_frame >= len(self.cached_surfaces):
            if self.permanent:
                self.current_frame = 0  # Loop animation
            else:
                self.kill()  # Remove if not permanent

        # Keep the ring centered on the reference point
        self.rect = self.image.get_rect(center=self.reference_point.rect.center)
