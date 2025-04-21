import pygame
from src.views.menu_base import MenuBase

class NameEntryMenu(MenuBase):
    def __init__(self, display, renderer, high_scores=None):
        super().__init__(display, renderer, high_scores)
        self.current_name = ""
        self.score = 0

    def draw(self):
        # Create name entry box
        menu_width = 400
        menu_height = 200
        menu_surface = pygame.Surface((menu_width, menu_height), pygame.SRCALPHA)
        pygame.draw.rect(menu_surface, (50, 50, 50, 200), (0, 0, menu_width, menu_height), border_radius=15)
        
        menu_x = self.display.get_width() // 2 - menu_width // 2
        menu_y = self.display.get_height() // 2 - menu_height // 2
        self.display.blit(menu_surface, (menu_x, menu_y))

        # Draw text
        text = self.menu_font_small.render("New High Score!", True, (210, 105, 30))
        score_text = self.menu_font_small.render(f"Score: {self.score}", True, (200, 200, 200))
        name_text = self.menu_font_small.render("Enter your name:", True, (200, 200, 200))
        input_text = self.menu_font_small.render(self.current_name + "_", True, (200, 200, 200))
        
        text_x = self.display.get_width() // 2 - text.get_width() // 2
        self.display.blit(text, (text_x, menu_y + 30))
        self.display.blit(score_text, (text_x, menu_y + 60))
        self.display.blit(name_text, (text_x, menu_y + 90))
        self.display.blit(input_text, (text_x, menu_y + 120))

        pygame.display.flip()