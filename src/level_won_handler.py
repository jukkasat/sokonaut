import pygame

class LevelWonHandler:
    def __init__(self, display, game_state, font):
        self.display = display
        self.game_state = game_state
        self.font = font

    def draw_level_won(self):
        # Create a semi-transparent background box for text
        menu_width = 400
        menu_height = 180
        menu_surface = pygame.Surface((menu_width, menu_height), pygame.SRCALPHA)

        # Draw rounded rectangle with alpha
        pygame.draw.rect(
            menu_surface,
            (50, 50, 50, 216),
            (0, 0, menu_width, menu_height),
            border_radius=15
        )

        # Position the menu background in center
        menu_x = self.display.get_width() // 2 - menu_width // 2
        menu_y = self.display.get_height() // 2 - menu_height // 2
        self.display.blit(menu_surface, (menu_x, menu_y))

        # Draw victory text
        text = self.font.render("Congrats, level won!", True, (210, 105, 30))
        text_x = self.display.get_width() // 2 - text.get_width() // 2
        text_y = menu_y + 30
        self.display.blit(text, (text_x, text_y))

        # Draw level score
        text = self.font.render(f"SCORE: {self.game_state.level_score}", True, (200, 200, 200))
        score_x = self.display.get_width() // 2 - text.get_width() // 2
        score_y = menu_y + 80
        self.display.blit(text, (score_x, score_y))

        # Add Next Level-button if not on last level
        if self.game_state.current_level < len(self.game_state.maps) - 1:
            next_text = self.font.render("Press ENTER to start next level", True, (200, 200, 200))
            next_x = self.display.get_width() // 2 - next_text.get_width() // 2
            next_y = menu_y + 130
            self.display.blit(next_text, (next_x, next_y))