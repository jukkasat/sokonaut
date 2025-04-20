import pygame

class UIDrawer:
    def __init__(self, display, game_state, font):
        self.display = display
        self.game_state = game_state
        self.font = font

    def draw_ui(self):
        # Draw semi-transparent strip at the bottom
        strip_height = 40  # Height of the strip
        strip = pygame.Surface((self.display.get_width(), strip_height), pygame.SRCALPHA)
        strip.fill((0, 0, 0, 188))  # Black with 50% transparency
        self.display.blit(strip, (0, self.display.get_height() - strip_height))

        # Draw UI elements below the game field
        ui_y = self.display.get_height() - 35  # Position 35 pixels from the bottom

        text = self.font.render(f"Level: {self.game_state.current_level}", True, (200, 200, 200))
        self.display.blit(text, (25, ui_y))

        text = self.font.render(f"Moves: {self.game_state.moves}", True, (210, 105, 30))
        self.display.blit(text, (150, ui_y))

        text = self.font.render(f"score: {self.game_state.total_score}", True, (200, 200, 200))
        self.display.blit(text, (self.display.get_width() // 2 - text.get_width() // 2, ui_y))

        text = self.font.render("F3 = Restart", True, (200, 200, 200))
        self.display.blit(text, (self.display.get_width() - text.get_width() - 170, ui_y))

        text = self.font.render("F2 = Menu", True, (200, 200, 200))
        self.display.blit(text, (self.display.get_width() - text.get_width() - 25, ui_y))
