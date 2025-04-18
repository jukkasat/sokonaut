import pygame
from views.menu_base import MenuBase

class HighScoresMenu(MenuBase):
    def __init__(self, display, renderer, high_scores=None):
        super().__init__(display, renderer, high_scores)

    def draw(self):
        self.display.fill((0, 0, 0))

        # Draw background
        self.draw_background()

        # Draw title
        title = self.menu_font.render("HIGH SCORES", True, (224, 127, 50))
        title_pos = (self.display.get_width() // 2 - title.get_width() // 2, 80)
        self.display.blit(title, title_pos)

        # Create background for scores
        menu_width = 400
        menu_height = 476
        menu_surface = pygame.Surface((menu_width, menu_height), pygame.SRCALPHA)
        pygame.draw.rect(menu_surface, (50, 50, 50, 200), (0, 0, menu_width, menu_height), border_radius=15)
        
        menu_x = self.display.get_width() // 2 - menu_width // 2
        menu_y = 180
        self.display.blit(menu_surface, (menu_x, menu_y))

        # Draw scores
        y_pos = menu_y + 30
        if self.high_scores is not None:
            for i, score in enumerate(self.high_scores.get_scores()):
                rank_text = self.menu_font_small.render(f"{i+1}.", True, (200, 200, 200))
                name_text = self.menu_font_small.render(score["name"], True, (200, 200, 200))
                score_text = self.menu_font_small.render(str(score["score"]), True, (200, 200, 200))
                
                self.display.blit(rank_text, (menu_x + 50, y_pos))
                self.display.blit(name_text, (menu_x + 100, y_pos))
                self.display.blit(score_text, (menu_x + 300, y_pos))
                y_pos += 40

        # Draw back text
        back_text = self.menu_font_small.render("Press ESC to return", True, (200, 200, 200))
        back_x = self.display.get_width() // 2 - back_text.get_width() // 2
        back_y = menu_y + menu_height - 40
        self.display.blit(back_text, (back_x, back_y))

        pygame.display.flip()

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "main_menu"
        return None