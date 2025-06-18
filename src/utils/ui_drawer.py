import pygame
from src.utils.helper import center_text

class UIDrawer:
    def __init__(self, display, game_state, font):
        self.display = display
        self.game_state = game_state
        self.font = font
        self.restart_rect = None
        self.quit_rect = None

    def draw_ui(self):
        # Draw semi-transparent strip at the bottom
        strip_height = 40  # Height of the strip
        strip = pygame.Surface((self.display.get_width(), strip_height), pygame.SRCALPHA)
        strip.fill((0, 0, 0, 188))  # Black with 50% transparency
        self.display.blit(strip, (0, self.display.get_height() - strip_height))

        # Draw UI elements below the game field
        ui_y = self.display.get_height() - 35  # Position 35 pixels from the bottom

        level_text = self.font.render(f"Level: {self.game_state.current_level}", True, (200, 200, 200))
        self.display.blit(level_text, (25, ui_y))

        moves_text = self.font.render(f"Moves: {self.game_state.moves}", True, (210, 105, 30))
        self.display.blit(moves_text, (150, ui_y))

        score_text = self.font.render(f"score: {self.game_state.total_score}", True, (200, 200, 200))
        self.display.blit(score_text, (self.display.get_width() // 2 - score_text.get_width() // 2, ui_y))

        # Store restart text rect for click detection
        restart_text = self.font.render("F3 = Restart", True, (200, 200, 200))
        restart_pos = (self.display.get_width() - restart_text.get_width() - 170, ui_y)
        self.restart_rect = restart_text.get_rect(topleft=restart_pos)
        self.display.blit(restart_text, restart_pos)

        # Store quit text rect for click detection  
        quit_text = self.font.render("F2 = Quit", True, (200, 200, 200))
        quit_pos = (self.display.get_width() - quit_text.get_width() - 25, ui_y)
        self.quit_rect = quit_text.get_rect(topleft=quit_pos)
        self.display.blit(quit_text, quit_pos)

    def draw_menu(self, menu_width, menu_height, menu_x, menu_y, text, score_text, next_text):
        menu_surface = pygame.Surface((menu_width, menu_height), pygame.SRCALPHA)

        # Draw rounded rectangle with alpha
        pygame.draw.rect(menu_surface,
            (50, 50, 50, 216),(0, 0, menu_width,
            menu_height),border_radius=15
        )
        self.display.blit(menu_surface, (menu_x, menu_y))

        # Draw victory text
        text_rect = center_text(self.display, text, menu_y + 50)
        self.display.blit(text, text_rect)

        # Draw level score
        score_rect = center_text(self.display, score_text, menu_y + 116)
        self.display.blit(score_text, score_rect)

        # Add Next Level-button if not on last level
        next_rect = center_text(self.display, next_text, menu_y + 160)
        self.display.blit(next_text, next_rect)