import pygame
from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        # Call the parent constructor with SHOT_RADIUS
        super().__init__(x, y, SHOT_RADIUS)

        # Set the initial velocity of the shot
        self.velocity = velocity

    def draw(self, screen):
        # Draw the shot as a small circle
        pygame.draw.circle(
            screen, "white", (int(self.position.x), int(self.position.y)), self.radius
        )

    def update(self, dt):
        # Update the position of the shot
        self.position += self.velocity * dt
