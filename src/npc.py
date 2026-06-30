import pygame
import os

class NPC: 
    """
    Represents a non-player character that can be talked to.
    """

    def __init__(self, x, y, name, sprite_path, dialogue):
        self.x = x
        self.y = y
        self.name = name
        self.width = 32
        self.height = 48

        # Dialogue is a list of strings - each one a line/page of text
        self.dialogue = dialogue
        self.dialogue_index = 0

        self.image = pygame.image.load(os.path.join(sprite_path))
    
    def get_rect(self):
        """Return pygame Rect representing his NPC's position and size."""
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def get_current_line(self):
        """Return current line of dialogue."""
        return self.dialogue[self.dialogue_index]
    
    def advance_dialogue(self):
        """
        Move to the next line of dialogue.
        Returns False if conversation ended. True if more remains.
        """
        self.dialogue_index += 1
        if self.dialogue_index >= len(self.dialogue):
            self.dialogue_index = 0
            return False
        return True
    def draw(self, screen):
        """Draw the NPC onto the screen."""
        screen.blit(self.image, (self.x, self.y))