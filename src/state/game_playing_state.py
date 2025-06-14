import pygame
import sys
from src.state.state import State

class GamePlayingState(State):
    def __init__(self, sokonaut):
        super().__init__(sokonaut)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                moved = False
                if event.key == pygame.K_LEFT:
                    self.sokonaut.game_state.move(0, -1)
                    moved = True
                if event.key == pygame.K_RIGHT:
                    self.sokonaut.game_state.move(0, 1)
                    moved = True
                if event.key == pygame.K_UP:
                    self.sokonaut.game_state.move(-1, 0)
                    moved = True
                if event.key == pygame.K_DOWN:
                    self.sokonaut.game_state.move(1, 0)
                    moved = True
                if moved:
                    self.sokonaut.audio_manager.play_sound("move")
                if event.key == pygame.K_F2:
                    self.sokonaut.current_state = self.sokonaut.main_menu_state
                    self.sokonaut.audio_manager.play_music("menu")
                    return "return_to_menu"
                if event.key == pygame.K_F3:
                    self.sokonaut.game_state.restart_level()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if self.sokonaut.game_state.game_completed():
            return "game_completed"
        elif self.sokonaut.game_state.level_won():
            return "level_won"

        return None

    def draw(self):
        self.sokonaut.renderer.draw()