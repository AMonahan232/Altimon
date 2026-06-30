import pygame

class DialogueBox:
    """
    Renders the text box at the bottom of the screen for NPC dialogue.
    """

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.box_height = 120
        self.padding = 20

        self.font = pygame.font.SysFont("Arial", 22)
        self.name_font = pygame.font.SysFont("Arial", 22, bold=True)

        self.bg_color = (20, 20, 20)
        self.border_color = (255, 255, 255)
        self.text_color = (255, 255, 255)

    def draw(self, screen, speaker_name, text):
        """Draw the dialogue box with speaker name and text."""
        box_y = self.screen_height - self.box_height - self.padding
        box_rect = pygame.Rect(
            self.padding,
            box_y,
            self.screen_width - (self.padding * 2),
            self.box_height
        )

        # Draw background and boarder.
        pygame.draw.rect(screen, self.bg_color, box_rect)
        pygame.draw.rect(screen, self.border_color, box_rect, 3)

        # Draw speaker name.
        name_surface = self.name_font.render(speaker_name, True, self.text_color)
        screen.blit(name_surface, (box_rect.x + 15, box_rect.y + 10))

        # Draw dialogue text.
        text_surface = self.font.render(text, True, self.text_color)
        screen.blit(text_surface, (box_rect.x + 15, box_rect.y + 45))

        # Draw a small prompt
        prompt_surface = self.font.render("Press SPACE to continue", True, (180, 180, 180))
        screen.blit(prompt_surface, (box_rect.x + 15, box_rect.y + 85))