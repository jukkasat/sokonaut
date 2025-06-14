import pygame
from src.state.state import State

class GameWonState(State):
    def __init__(self, sokonaut):
        super().__init__(sokonaut)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F2:
                    self.sokonaut.current_state = self.sokonaut.main_menu_state
                    self.sokonaut.audio_manager.play_music("menu")
                    return None
        return None

    def draw(self):
        self.sokonaut.renderer.draw()