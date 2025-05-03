import pygame
import sys
from src.game_state import GameState
from src.renderer import Renderer
from src.handlers.input_handler import InputHandler
from src.menu import Menu
from src.scores import Scores
from src.utils.audio_manager import AudioManager

class Sokonaut:

    def __init__(self):
        # Initialize pygame and set up the game window
        pygame.init()
        self.screen_width = 1280
        self.screen_height = 720
        self.display = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Sokonaut")

        # Initialize game components
        self.audio_manager = AudioManager() # Handles audio
        self.game_state = GameState(self.audio_manager)  # Manages the game state
        self.scores = Scores()
        self.renderer = Renderer(self.game_state, self.display, self.scores)  # Handles rendering
        self.input_handler = InputHandler(self.game_state, self.scores, self.audio_manager)  # Handles user input
        self.menu = Menu(self.display, self.renderer, self.scores, self.audio_manager)  # Manages the menu

        self.audio_manager.play_music("menu")
        
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
                    self.audio_manager.play_music("level")
                elif action and action.startswith("start_level_"):
                    level = int(action.split("_")[-1])
                    if self.scores.is_level_unlocked(level):
                        self.game_state.start_level(level)
                        self.game_state._update_dimensions()
                        self.renderer.update_scaling()
                        self.menu.in_menu = False
                        self.audio_manager.play_music("level")
                    else:
                        print("Level is locked!")
                elif action == "high_score":
                    self.menu.active_menu = "high_score"
                    self.audio_manager.pause_music()
                elif action == "levels":
                    self.menu.active_menu = "levels"
                    self.audio_manager.pause_music()
                self.menu.draw()
            else:
                action = self.input_handler.handle_events()
                if action == "return_to_menu":
                    # Check for high score before returning to menu
                    if (self.game_state.total_score > 0 and 
                        self.scores.is_high_score(self.game_state.total_score)):
                        self.menu.active_menu = "name_entry"
                        self.menu.name_entry_menu.score = self.game_state.total_score
                        self.menu.name_entry_menu.current_name = self.menu.current_name
                        self.menu.draw()
                        self.audio_manager.pause_music()

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
                                    self.scores.add_score(self.menu.name_entry_menu.current_name, self.game_state.total_score)
                                    self.menu.current_name = self.menu.name_entry_menu.current_name
                                    entering_name = False
                                    self.menu.in_menu = True
                                    self.menu.active_menu = "main_menu"
                                    self.audio_manager.play_music("menu")
                                elif event.key == pygame.K_ESCAPE:
                                    entering_name = False
                                    self.menu.in_menu = True
                                    self.menu.active_menu = "main_menu"
                                    self.audio_manager.play_music("menu")
                                elif len(self.menu.name_entry_menu.current_name) < 15:
                                    if event.unicode.isalnum():
                                        self.menu.name_entry_menu.current_name += event.unicode
                            self.menu.draw()
                    else:
                        self.menu.in_menu = True
                        self.menu.active_menu = "main_menu"
                        self.audio_manager.play_music("menu")
            if not self.menu.in_menu:
                self.renderer.draw()
