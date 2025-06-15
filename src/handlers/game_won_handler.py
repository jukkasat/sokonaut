import pygame
from src.utils.helper import center_rect

class GameWonHandler:
    def __init__(self, display, game_state, font, image_loader, ui_drawer):
        self.display = display
        self.game_state = game_state
        self.font = font
        self.image_loader = image_loader
        self.ui_drawer = ui_drawer
        self.large_font = pygame.font.SysFont("Arial", 36)

    def draw_game_won(self):
        # Draw level won background
        if self.image_loader.game_won_background:
            self.display.blit(self.image_loader.game_won_background, (0, 0))

        menu_width = 400
        menu_height = 220
        menu_x, menu_y = center_rect(self.display, menu_width, self.display.get_height() // 2 - menu_height // 2)

        text = self.large_font.render("Game won, good job!", True, (210, 105, 30))
        score_text = self.font.render(f"TOTAL SCORE: {self.game_state.total_score}", True, (200, 200, 200))
        menu_text = self.font.render("F2 to Main menu", True, (200, 200, 200))
        
        self.ui_drawer.draw_menu(menu_width, menu_height, menu_x, menu_y, text, score_text, menu_text)
