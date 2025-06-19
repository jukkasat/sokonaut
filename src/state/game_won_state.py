
import sys
import pygame
from src.state.state import State

class GameWonState(State):
    def __init__(self, sokonaut):
        super().__init__(sokonaut)

    def handle_input(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_F2, pygame.K_RETURN, pygame.K_ESCAPE):
                    self.__return_to_menu()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.sokonaut.renderer.ui_drawer.quit_rect and \
                self.sokonaut.renderer.ui_drawer.quit_rect.collidepoint((event.pos)):
                    self.__return_to_menu()
                # Check click on "Enter to Main menu" text
                if hasattr(self.sokonaut.renderer.game_won_view, "menu_text_rect"):
                    if self.sokonaut.renderer.game_won_view.menu_text_rect.collidepoint(event.pos):
                        self.__return_to_menu()
        return None

    def __return_to_menu(self):
        self.sokonaut.audio_manager.play_sound("select")
        self.sokonaut.current_state = self.sokonaut.main_menu_state

    def draw(self):
        self.sokonaut.renderer.draw()