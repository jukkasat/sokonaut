import pygame
import sys
from src.game_state import GameState
from src.renderer import Renderer
from src.input_handler import InputHandler
from src.menu import Menu
from src.high_scores import HighScores

class Sokonaut:

    def __init__(self):
        # Initialize pygame and set up the game window
        pygame.init()
        self.screen_width = 1280
        self.screen_height = 720
        self.display = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Sokonaut")

        # Initialize game components
        self.game_state = GameState()  # Manages the game state
        self.renderer = Renderer(self.game_state, self.display)  # Handles rendering
        self.input_handler = InputHandler(self.game_state)  # Handles user input
        self.menu = Menu(self.display, self.renderer)  # Manages the menu
        self.high_scores = HighScores()
        self.menu = Menu(self.display, self.renderer, self.high_scores)

        # Start the main game loop
        self.loop()

    def loop(self):
        while True:
            if self.menu.in_menu:
                action = self.menu.handle_input()
                if action == "new_game":
                    self.game_state.new_game()
                    self.game_state._update_dimensions()
                    self.renderer.update_scaling()
                    self.menu.in_menu = False
                elif action and action.startswith("start_level_"):
                    level = int(action.split("_")[-1])
                    self.game_state.start_level(level)
                    self.game_state._update_dimensions()
                    self.renderer.update_scaling()
                    self.menu.in_menu = False
                elif action == "high_score":
                    self.menu.active_menu = "high_score"
                elif action == "levels":
                    self.menu.active_menu = "levels"
                self.menu.draw()
            else:
                action = self.input_handler.handle_events()
                if action == "return_to_menu":
                    # Check for high score before returning to menu
                    if (self.game_state.total_score > 0 and 
                        self.high_scores.is_high_score(self.game_state.total_score)):
                        self.menu.active_menu = "name_entry"
                        self.menu.name_entry_menu.score = self.game_state.total_score
                        self.menu.name_entry_menu.current_name = self.menu.current_name
                        self.menu.draw()

                        # Handle name entry input
                        entering_name = True
                        while entering_name:
                            event = pygame.event.wait()
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_BACKSPACE:
                                    self.menu.name_entry_menu.current_name = self.menu.name_entry_menu.current_name[:-1]
                                elif event.key == pygame.K_RETURN:
                                    self.high_scores.add_score(self.menu.name_entry_menu.current_name, self.game_state.total_score)
                                    self.menu.current_name = self.menu.name_entry_menu.current_name
                                    entering_name = False
                                    self.menu.in_menu = True
                                    self.menu.active_menu = "main_menu"
                                elif event.key == pygame.K_ESCAPE:
                                    entering_name = False
                                    self.menu.in_menu = True
                                    self.menu.active_menu = "main_menu"
                                elif len(self.menu.name_entry_menu.current_name) < 15:
                                    if event.unicode.isalnum():
                                        self.menu.name_entry_menu.current_name += event.unicode
                            self.menu.draw()
                    else:
                        self.menu.in_menu = True
                        self.menu.active_menu = "main_menu"
            if not self.menu.in_menu:
                self.renderer.draw()
