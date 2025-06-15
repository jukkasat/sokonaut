import pygame
from src.utils.helper import center_rect

class LevelWonHandler:
    def __init__(self, display, game_state, font, scores, ui_drawer):
        self.display = display
        self.game_state = game_state
        self.font = font
        self.scores = scores
        self.ui_drawer = ui_drawer
        self.large_font = pygame.font.SysFont("Arial", 36)

    def draw_level_won(self):
        # Create a semi-transparent background box for text
        menu_width = 400
        menu_height = 220
        menu_x, menu_y = center_rect(self.display, menu_width, self.display.get_height() // 2 - menu_height // 2)

        text = self.large_font.render("Congrats, level won!", True, (210, 105, 30))
        score_text = self.font.render(f"SCORE: {self.game_state.level_score}", True, (200, 200, 200))
        if self.game_state.current_level < len(self.game_state.maps) - 1:
            next_text = self.font.render("Press ENTER to start next level", True, (200, 200, 200))

        self.ui_drawer.draw_menu(menu_width, menu_height, menu_x, menu_y, text, score_text, next_text)
