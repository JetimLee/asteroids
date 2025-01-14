import pygame
from constants import *
from player import Player  # Import the Player class

# Create groups for updatable and drawable objects
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

# Add static containers field to the Player class
Player.containers = (updatable, drawable)


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

    # Main game loop
    while True:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop

        # Update all updatable objects
        for obj in updatable:
            obj.update(dt)

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
