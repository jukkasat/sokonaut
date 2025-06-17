import pygame
from src.views.menu_base import MenuBase
from src.utils.helper import center_text, center_rect

class HighScoresMenu(MenuBase):
    def __init__(self, display, renderer, scores):
        super().__init__(display, renderer, scores)
        self.background_image = self.load_menu_background()

    def draw(self):
        self.display.fill((0, 0, 0))

        # Draw background image
        if self.background_image:
            self.display.blit(self.background_image, (0, 0))

        # Draw title
        title = self.menu_font.render("HIGH SCORES", True, (255, 130, 0))
        title_rect = center_text(self.display, title, 100)
        self.display.blit(title, title_rect)

        # Create background for scores
        menu_width = 400
        menu_height = 476
        menu_x, menu_y = center_rect(self.display, menu_width, 170)
        self.draw_menu_background(menu_width, menu_height, menu_x, menu_y)

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

        # Draw and store back button position for mouse interaction
        back_text = self.menu_font_small.render("BACK", True, (210, 105, 30))
        back_rect = center_text(self.display, back_text, menu_y + menu_height - 45)
        self.back_rect = back_text.get_rect(topleft=(back_rect.x, back_rect.y))
        self.display.blit(back_text, back_rect)

        pygame.display.flip()

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "main_menu"
            
        # Handle mouse input
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                mouse_pos = pygame.mouse.get_pos()
                if self.back_rect.collidepoint(mouse_pos):
                    return "main_menu"
        return None