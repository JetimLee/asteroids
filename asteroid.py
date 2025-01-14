import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call the parent constructor
        super().__init__(x, y, radius)

    def draw(self, screen):
        # Draw the asteroid as a circle
        pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            self.radius,
            2,
        )

    def update(self, dt):
        # Move the asteroid in a straight line
        self.position += self.velocity * dt

    def split(self):
        """Split the asteroid into two smaller ones or destroy it if it's too small."""
        # Remove the current asteroid
        self.kill()

        # If the asteroid is too small, don't split further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Generate a random angle for splitting
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating the current velocity
        velocity1 = self.velocity.rotate(random_angle) * 1.2  # Scale up the speed
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Calculate the new radius for smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new asteroids
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity2
