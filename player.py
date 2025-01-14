from circleshape import CircleShape
import pygame
from constants import *
from shot import Shot  # Import the Shot class


# Base class for player objects
class Player(CircleShape):
    def __init__(self, x, y, radius):
        # Call the parent class constructor
        super().__init__(x, y, radius)

        # Initialize rotation
        self.rotation = 0
        self.shoot_timer = 0  # Timer to manage shooting cooldown

    # The triangle method to calculate the player's shape
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt, reverse=False):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        direction = -1 if reverse else 1  # Reverse the direction for backward movement
        self.position += forward * PLAYER_SPEED * dt * direction

    def shoot(self):
        if self.shoot_timer > 0:
            return  # Prevent shooting if the timer is active

        # Get the front tip of the triangle
        front_tip = self.triangle()[
            0
        ]  # The first point in the triangle is the front tip

        # Calculate the velocity of the shot
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Forward direction
        velocity = forward * PLAYER_SHOOT_SPEED  # Scale up velocity

        # Create a new shot at the front tip of the triangle
        Shot(front_tip.x, front_tip.y, velocity)

        # Reset the shoot timer
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    # Override the draw method
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # Update method to handle input
    def update(self, dt):
        # Decrease the shoot timer
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate left
        if keys[pygame.K_d]:
            self.rotate(dt)  # Rotate right
        if keys[pygame.K_w]:
            self.move(dt)  # Move forward
        if keys[pygame.K_s]:
            self.move(dt, reverse=True)  # Move backward
        if keys[pygame.K_SPACE]:
            self.shoot()  # Fire a shot
