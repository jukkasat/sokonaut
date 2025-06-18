import sys
import pygame
from src.state.menu_state import MenuState

class HighScoreState(MenuState):
    def __init__(self, sokonaut):
        super().__init__(sokonaut)
        self.menu = sokonaut.menu.high_scores_menu

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                    self._return_to_menu()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    mouse_pos = pygame.mouse.get_pos()
                    if self.menu.back_rect.collidepoint(mouse_pos):
                        self._return_to_menu()

        return None

    def draw(self):
        self.sokonaut.menu.high_scores_menu.draw()