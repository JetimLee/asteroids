import pygame
from constants import *
from player import Player  # Import the Player class
from asteroid import Asteroid  # Import the Asteroid class
from asteroidfield import AsteroidField  # Import the AsteroidField class
from shot import Shot  # Import the Shot class

# Create groups for updatable, drawable, asteroid objects, and shots
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

# Add static containers field to the Player, Asteroid, and AsteroidField classes
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
Shot.containers = (shots, updatable, drawable)  # Shots included in relevant groups
AsteroidField.containers = (updatable,)  # Only updatable


def main():
    # Initialize pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    # Print statements
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create a clock object and initialize dt
    clock = pygame.time.Clock()
    dt = 0

    # Instantiate the Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    # Create the AsteroidField object
    asteroid_field = AsteroidField()  # Handles spawning and managing asteroids

    # Main game loop
    while True:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()  # Call the shoot method when SPACE is pressed

        # Update all updatable objects
        for obj in updatable:
            obj.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return  # Exit the program

            # Check for collisions between shots and asteroids
            for shot in shots:
                if shot.collides_with(asteroid):
                    print(f"Asteroid destroyed at {asteroid.position}!")
                    asteroid.split()  # Call the split method instead of kill
                    shot.kill()  # Remove the shot

        # Fill the screen with a solid black color
        screen.fill((0, 0, 0))  # RGB for black

        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        # Refresh the display
        pygame.display.flip()

        # Cap the frame rate at 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000  # Returns milliseconds, converted to seconds


if __name__ == "__main__":
    main()
