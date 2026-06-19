import pygame
import os

class Player:
    """
    Represents the player character in Altimon.
    Handles movement, rendering, and player state.
    """

    def __init__(self, x, y, name="Trainer"):
        # Position
        self.x = x
        self.y = y

        # Settings
        self.name = name
        self.speed = 3
        self.width = 32
        self.height = 48

        # Load Sprite
        self.image = pygame.image.load(
            os.path.join("../assets/sprites/player.png")
        )

    def handle_input(self, keys):
        """Move the player based on keyboard input."""
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def apply_bounderies(self, screen_width, screen_height):
        """Keep the player inside the screen."""
        if self.x < 0:
            self.x = 0
        if self.x > screen_width - self.width:
            self.x = screen_width - self.width
        if self.y < 0:
            self.y = 0
        if self.y > screen_height - self.height:
            self.y = screen_height - self.height

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
