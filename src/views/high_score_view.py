import pygame
from src.views.menu_base import MenuBase

class HighScoresMenu(MenuBase):
    def __init__(self, display, renderer, scores=None):
        super().__init__(display, renderer, scores)
        self.background_image = self.load_menu_background()

    def draw(self):
        self.display.fill((0, 0, 0))

        # Draw background image
        if self.background_image:
            self.display.blit(self.background_image, (0, 0))

        # Draw title
        title = self.menu_font.render("HIGH SCORES", True, (255, 130, 0))
        title_pos = (self.display.get_width() // 2 - title.get_width() // 2, 60)
        self.display.blit(title, title_pos)

        # Create background for scores
        menu_width = 400
        menu_height = 476
        menu_surface = pygame.Surface((menu_width, menu_height), pygame.SRCALPHA)
        pygame.draw.rect(menu_surface, (50, 50, 50, 200), (0, 0, menu_width, menu_height), border_radius=15)
        
        menu_x = self.display.get_width() // 2 - menu_width // 2
        menu_y = 170
        self.display.blit(menu_surface, (menu_x, menu_y))

        # Draw scores
        y_pos = menu_y + 30
        if self.scores is not None:
            scores = self.scores.get_scores()
            for i, score in enumerate(scores):
                if i == 0:  # First place: Gold
                    color = (212, 175, 55)
                    font = pygame.font.SysFont("Arial", 22)
                else:  # Other scores
                    color = (200, 200, 200)
                    font = self.menu_font_small
                
                rank_text = font.render(f"{i+1}.", True, color)
                name_text = font.render(score["name"], True, color)
                score_text = font.render(str(score["score"]), True, color)
                
                self.display.blit(rank_text, (menu_x + 50, y_pos))
                self.display.blit(name_text, (menu_x + 100, y_pos))
                self.display.blit(score_text, (menu_x + 300, y_pos))
                y_pos += 40

        # Draw back button
        back_text = self.menu_font_small.render("BACK", True, (210, 105, 30))
        back_x = self.display.get_width() // 2 - back_text.get_width() // 2
        back_y = menu_y + menu_height - 45
        self.display.blit(back_text, (back_x, back_y))

        pygame.display.flip()

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "main_menu"        
        return None