import pygame
import sys
import os
from player import Player
from tilemap import Tilemap
from npc import NPC
from dialogue_box import DialogueBox

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Altimon")
clock = pygame.time.Clock()

# Game objects
tilemap = Tilemap(
    map_path=os.path.join("../assets/maps/island1.csv"),
    tile_size=32
)
player = Player(x=300, y=300, name="Trainer")

mentor = NPC(
    x=400,
    y=200,
    name="Professor Hale",
    sprite_path="../assets/sprites/mentor.png",
    dialogue=[
        "Ah, you must be the one I've heard about.",
        "I've spent my life studying the Altimons since the comet storm.",
        "The Eclipse Order seeks to control them and bring ruin to our world.",
        "I believe you may be the one who can stop them.",
        "Take this Altimon and begin your journey."
    ]
)

dialogue_box = DialogueBox(SCREEN_WIDTH, SCREEN_HEIGHT)

# Dialogue state
in_dialogue = False
active_npc = None

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if in_dialogue:
                    # Advance dialogue or end conversation
                    has_more = active_npc.advance_dialogue()
                    if not has_more:
                        in_dialogue = False
                        active_npc = None
                else:
                    # Check if player is near the mentor to start dialogue
                    player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
                    mentor_rect = mentor.get_rect()

                    # Expand mentor's rect slightly to create an interaction range
                    interaction_rect = mentor_rect.inflate(20, 20)

                    if player_rect.colliderect(interaction_rect):
                        in_dialogue = True
                        active_npc = mentor

    # Only allow movement when not in dialogue
    if not in_dialogue:
        keys = pygame.key.get_pressed()
        player.handle_input(keys, tilemap)
        player.apply_boundaries(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Draw everything
    screen.fill(BLACK)
    tilemap.draw(screen)
    mentor.draw(screen)
    player.draw(screen)

    if in_dialogue:
        dialogue_box.draw(screen, active_npc.name, active_npc.get_current_line())

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()