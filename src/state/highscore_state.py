import pygame
from src.state.menu_state import MenuState

class HighScoreState(MenuState):
    def __init__(self, sokonaut):
        super().__init__(sokonaut)
        self.menu = sokonaut.menu.high_scores_menu

    def handle_input(self):
        for event in pygame.event.get():
            action = self.sokonaut.menu.high_scores_menu.handle_input(event)
            if action == "main_menu":
                self.sokonaut.audio_manager.play_sound("select")
                self.sokonaut.current_state = self.sokonaut.main_menu_state
                return None
        return None

    def draw(self):
        self.sokonaut.menu.high_scores_menu.draw()