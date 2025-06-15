import pygame
from src.state.menu_state import MenuState

class LevelsMenuState(MenuState):
    def __init__(self, sokonaut):
        super().__init__(sokonaut)
        self.menu = sokonaut.menu.levels_menu

    def handle_input(self):
        for event in pygame.event.get():
            action = self.sokonaut.menu.levels_menu.handle_input(event)
            if action == "main_menu":
                self.sokonaut.audio_manager.play_sound("select")
                self.sokonaut.current_state = self.sokonaut.main_menu_state
                return None
            elif action is not None:
                self.sokonaut.audio_manager.play_sound("select")
                return action
        return None

    def draw(self):
        self.sokonaut.menu.levels_menu.draw()