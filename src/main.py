import pygame
import sys
import os

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

#Player Starting Position
player_x = 100
player_y = 100
PLAYER_SPEED = 3

# Load player sprite
player_image = pygame.image.load(
    os.path.join("../assets/sprites/player.png")
)

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
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_x += PLAYER_SPEED
    if keys[pygame.K_UP]:
        player_y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player_y += PLAYER_SPEED

    # Keep player inside screen boundaries
    if player_x < 0:
        player_x = 0
    if player_x > SCREEN_WIDTH - 32:    # 32 = player width
        player_x = SCREEN_WIDTH - 32
    if player_y < 0:
        player_y = 0
    if player_y > SCREEN_HEIGHT - 32:   # 32 = player height
        player_y = SCREEN_HEIGHT - 32

    #3. Draw Everything
    screen.fill(BLACK)
    screen.blit(player_image, (player_x, player_y))
    pygame.display.flip()

    #4. Cap the Frame Rate
    clock.tick(FPS)

pygame.quit()
sys.exit()

