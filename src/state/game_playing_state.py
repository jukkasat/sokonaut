import pygame
from src.state.state import State
from src.views.mobile_controls import MobileControls

class GamePlayingState(State):
    def __init__(self, sokonaut):
        super().__init__(sokonaut)
        self.mobile_controls = MobileControls(sokonaut.display)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return self._return_to_menu()
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
                if event.key == pygame.K_F3:
                    self.sokonaut.game_state.restart_level()
                if event.key in (pygame.K_ESCAPE, pygame.K_F2):
                    return self._return_to_menu()

            # Handle touch/mouse input
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # Handle button controls
                direction = self.mobile_controls.handle_touch((x, y))
                if direction:
                    moved = False
                    if direction == "left":
                        self.sokonaut.game_state.move(0, -1)
                        moved = True
                    elif direction == "right":
                        self.sokonaut.game_state.move(0, 1)
                        moved = True
                    elif direction == "up":
                        self.sokonaut.game_state.move(-1, 0)
                        moved = True
                    elif direction == "down":
                        self.sokonaut.game_state.move(1, 0)
                        moved = True
                    if moved:
                        self.sokonaut.audio_manager.play_sound("move")

                # Check UI text clicks
                if self.sokonaut.renderer.ui_drawer.restart_rect and \
                self.sokonaut.renderer.ui_drawer.restart_rect.collidepoint((x, y)):
                    self.sokonaut.game_state.restart_level()
                    return None

                if self.sokonaut.renderer.ui_drawer.quit_rect and \
                self.sokonaut.renderer.ui_drawer.quit_rect.collidepoint((x, y)):
                    return self._return_to_menu()
            
        if self.sokonaut.game_state.game_completed():
            return "game_completed"
        elif self.sokonaut.game_state.level_won():
            return "level_won"

        return None

    def draw(self):
        self.sokonaut.renderer.draw()
        self.mobile_controls.draw()
