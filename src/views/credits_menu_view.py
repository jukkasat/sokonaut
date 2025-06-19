import os
import pygame
from src.views.menu_base import MenuBase
from src.utils.helper import center_text, center_rect

class CreditsMenu(MenuBase):
    def __init__(self, display, renderer, scores):
        super().__init__(display, renderer, scores)
        self.background_image = self.load_menu_background()
        self.back_rect = None

    def draw(self):
        self.display.fill((0, 0, 0))

        if self.background_image:
            self.display.blit(self.background_image, (0, 0))

        # Draw title
        title = self.menu_font.render("CREDITS", True, (255, 130, 0))
        title_rect = center_text(self.display, title, 100)
        self.display.blit(title, title_rect)

        # Create credits view background
        menu_width = 400
        menu_height = 470
        menu_x, menu_y = center_rect(self.display, menu_width, 170)
        self.draw_menu_background(menu_width, menu_height, menu_x, menu_y)

        # Draw credits text
        credits_text = [
            "developer",
            "jukkas",
            "",
            "For more games donate with Bolt 12"
        ]

        y_pos = menu_y + 38
        for text in credits_text:
            rendered_text = self.menu_font_small.render(text, True, (200, 200, 200))
            text_rect = center_text(self.display, rendered_text, y_pos)
            self.display.blit(rendered_text, text_rect)
            y_pos += 20

        # Load and draw tip image
        try:
            tip_image = pygame.image.load(os.path.join(self._get_base_path(), "tip.png"))
            # Scale image if needed (optional)
            tip_image = pygame.transform.scale(tip_image, (280, 280))  # Adjust size as needed
            
            # Center the image horizontally and place it below the text
            tip_rect = tip_image.get_rect()
            tip_rect.centerx = self.display.get_width() // 2
            tip_rect.top = y_pos + 10  # Add some padding between text and image
            
            self.display.blit(tip_image, tip_rect)
        except pygame.error as e:
            print(f"Could not load tip image: {e}")

        # Draw back button
        back_text = self.menu_font_small.render("BACK", True, (210, 105, 30))
        self.back_rect = center_text(self.display, back_text, menu_y + menu_height - 35)
        self.back_rect = back_text.get_rect(topleft=(self.back_rect.x, self.back_rect.y))
        self.display.blit(back_text, self.back_rect)
