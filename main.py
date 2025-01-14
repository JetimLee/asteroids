import pygame
from constants import *


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

    # Main game loop
    while True:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop

        # Fill the screen with a solid black color
        screen.fill((0, 0, 0))  # RGB for black

        # Refresh the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
