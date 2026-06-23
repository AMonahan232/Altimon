import pygame
import sys
from player import Player
from tilemap import Tilemap


# Initialize pygame
pygame.init()

# Window Settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# COLORS (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
BLUE = (70, 130, 180)
RED = (200, 50, 50)

# Create Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Altimon")

# Clock to control frame rate
clock = pygame.time.Clock()

#Create Game Objects
tilemap = Tilemap(tile_size=32)
player = Player(x=100, y=100, name="Trainer")

# Game Loop
running = True
while running:

    #1. Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #2. Update Gane Stats
    keys = pygame.key.get_pressed()
    player.handle_input(keys)
    player.apply_bounderies(SCREEN_WIDTH, SCREEN_HEIGHT)

    #3. Draw 
    screen.fill(BLACK)
    tilemap.draw(screen)
    player.draw(screen)
    pygame.display.flip()

    #4. Cap the Frame Rate
    clock.tick(FPS)

pygame.quit()
sys.exit()

