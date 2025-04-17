import sys
import pygame

class InputHandler:
    def __init__(self, game_state):
        self.game_state = game_state
    
    def handle_events(self):
        # Handle user input and events
        for event in pygame.event.get():
            # Handle key presses for movement and game controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game_state.move(0, -1)
                if event.key == pygame.K_RIGHT:
                    self.game_state.move(0, 1)
                if event.key == pygame.K_UP:
                    self.game_state.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    self.game_state.move(1, 0)
                if event.key == pygame.K_F2:
                    return "return_to_menu"
                if event.key == pygame.K_F3 and not (self.game_state.level_won() or self.game_state.game_completed()):
                    self.game_state.restart_level()
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_SPACE and self.game_state.level_won():
                    if self.game_state.current_level < len(self.game_state.maps) - 1:
                        self.game_state.current_level += 1
                        self.game_state.map = self.game_state.maps[self.game_state.current_level]
                        self.game_state.moves = 0

            if event.type == pygame.QUIT:
                sys.exit()