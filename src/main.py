import pygame
import sys

# Initialize pygame
pygame.init()

# Window Settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# COLORS (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Altimon")

# Clock to control frame rate
clock = pygame.time.Clock()

# Game Loop
running = True
while running:

    #1. Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #2. Update Gane Stats

    #3. Draw Everything
    screen.fill(BLACK)
    pygame.display.flip()

    #4. Cap the Frame Rate
    clock.tick(FPS)

pygame.quit()
sys.exit()

