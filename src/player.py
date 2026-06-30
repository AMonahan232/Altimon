import pygame
import os

class Player:
    """
    Represents the player character in Altimon.
    Handles movement, rendering, and collision detection.
    """

    def __init__(self, x, y, name="Trainer"):
        self.x = x
        self.y = y
        self.name = name
        self.speed = 3
        self.width = 32
        self.height = 48

        self.image = pygame.image.load(
            os.path.join("../assets/sprites/player.png")
        )

    def handle_input(self, keys, tilemap, npcs=None):
        """Move player based on input, respecting collision on all corners."""
        new_x = self.x
        new_y = self.y

        if keys[pygame.K_LEFT]:
            new_x -= self.speed
        if keys[pygame.K_RIGHT]:
            new_x += self.speed
        if keys[pygame.K_UP]:
            new_y -= self.speed
        if keys[pygame.K_DOWN]:
            new_y += self.speed

        if not self.is_colliding(new_x, new_y, tilemap, npcs):
            self.x = new_x
        
        if not self.is_colliding(new_x, new_y, tilemap, npcs):
            self.y = new_y

    def is_colliding(self, new_x, new_y, tilemap, npcs=None):
        """
        Check all four corners of the player against solid tiles.
        Returns True if any corner overlaps a solid tile.
        """
        tile_size = tilemap.tile_size

        corners = [
            (new_x, new_y),
            (new_x + self.width - 1, new_y),
            (new_x, new_y + self.height - 1),
            (new_x + self.width - 1, new_y + self.height - 1)
        ]

        for corner_x, corner_y in corners:
            grid_x = corner_x // tile_size
            grid_y = corner_y // tile_size
            if tilemap.is_solid(grid_x, grid_y):
                return True

        # Check collision against NPCs using their rects
        if npcs:
            player_rect = pygame.Rect(new_x, new_y, self.width, self.height)
            for npc in npcs:
                if player_rect.colliderect(npc.get_rect()):
                    return True
            
        return False

    def apply_boundaries(self, screen_width, screen_height):
        """Keep player inside screen boundaries."""
        if self.x < 0:
            self.x = 0
        if self.x > screen_width - self.width:
            self.x = screen_width - self.width
        if self.y < 0:
            self.y = 0
        if self.y > screen_height - self.height:
            self.y = screen_height - self.height

    def draw(self, screen):
        """Draw the player onto the screen."""
        screen.blit(self.image, (self.x, self.y))