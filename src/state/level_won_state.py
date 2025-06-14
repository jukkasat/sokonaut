import pygame
from src.state.state import State


class LevelWonState(State):
    def __init__(self, sokonaut):
        super().__init__(sokonaut)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F2:
                    self.sokonaut.current_state = self.sokonaut.main_menu_state
                    self.sokonaut.audio_manager.play_music("menu")
                    return "return_to_menu"
                elif event.key == pygame.K_RETURN:
                    result = self.sokonaut.game_state.complete_level()
                    if result == "next_level":
                        self.sokonaut.scores.mark_level_completed(self.sokonaut.game_state.current_level - 1)
                        return "next_level"
                    elif result == "game_completed":
                        return "game_completed"
        return None

    def draw(self):
        self.sokonaut.renderer.draw()
