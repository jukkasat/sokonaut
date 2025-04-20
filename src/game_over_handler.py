import pygame

class GameOverHandler:
    def __init__(self, display, game_state, font, image_loader):
        self.display = display
        self.game_state = game_state
        self.font = font
        self.image_loader = image_loader

    def draw_game_over(self):
        # Draw level won background
        if self.image_loader.game_won_background:
            self.display.blit(self.image_loader.game_won_background, (0, 0))

        # Create a semi-transparent background box for text
        menu_width = 400
        menu_height = 200
        menu_surface = pygame.Surface((menu_width, menu_height), pygame.SRCALPHA)

        # Draw rounded rectangle with alpha
        pygame.draw.rect(
            menu_surface,
            (50, 50, 50, 216),  # Semi-transparent dark background
            (0, 0, menu_width, menu_height),
            border_radius=15
        )

        # Position the menu background in center
        menu_x = self.display.get_width() // 2 - menu_width // 2
        menu_y = self.display.get_height() // 2 - menu_height // 2
        self.display.blit(menu_surface, (menu_x, menu_y))

        # Draw game won text
        text = self.font.render("Game won, good job!", True, (210, 105, 30))
        text_x = self.display.get_width() // 2 - text.get_width() // 2
        text_y = menu_y + 30
        self.display.blit(text, (text_x, text_y))

        # Draw total score
        score_text = self.font.render(f"TOTAL SCORE: {self.game_state.total_score}", True, (200, 200, 200))
        score_x = self.display.get_width() // 2 - score_text.get_width() // 2
        score_y = menu_y + 90
        self.display.blit(score_text, (score_x, score_y))

        # Draw options text
        menu_text = self.font.render("F2 to Main menu", True, (200, 200, 200))
        menu_x = self.display.get_width() // 2 - menu_text.get_width() // 2
        menu_y = menu_y + 180
        self.display.blit(menu_text, (menu_x, menu_y - 30))
