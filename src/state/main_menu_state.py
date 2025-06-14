import pygame
from src.state.menu_state import MenuState

class MainMenuState(MenuState):
    def __init__(self, sokonaut):
        super().__init__(sokonaut)
        self.menu = sokonaut.menu.main_menu

    def handle_input(self):
        action = self.sokonaut.menu.main_menu.handle_input(pygame.event.wait())
        if action == "new_game":
            self.sokonaut.audio_manager.play_sound("select")
            return "new_game"
        elif action == "levels":
            self.sokonaut.audio_manager.play_sound("select")
            self.sokonaut.current_state = self.sokonaut.levels_menu_state
            return None
        elif action == "high_score":
            self.sokonaut.audio_manager.play_sound("select")
            self.sokonaut.current_state = self.sokonaut.high_score_state
            return None
        elif action is not None:
            self.sokonaut.audio_manager.play_sound("select")
            return action
        return None

    def draw(self):
        self.sokonaut.menu.main_menu.draw()