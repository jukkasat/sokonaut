import pygame
from src.game_state import GameState
from src.renderer import Renderer
from src.menu import Menu
from src.state.main_menu_state import MainMenuState
from src.state.levels_menu_state import LevelsMenuState
from src.state.highscore_state import HighScoreState
from src.state.name_entry_state import NameEntryState
from src.state.game_playing_state import GamePlayingState
from src.state.level_won_state import LevelWonState
from src.state.game_won_state import GameWonState
from src.state.credits_state import CreditsState
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
        self.menu = Menu(self.display, self.renderer, self.scores)  # Manages the menu

        # Initialize states
        self.main_menu_state = MainMenuState(self)
        self.levels_menu_state = LevelsMenuState(self)
        self.high_score_state = HighScoreState(self)
        self.name_entry_state = NameEntryState(self)
        self.game_playing_state = GamePlayingState(self)
        self.level_won_state = LevelWonState(self)
        self.game_won_state = GameWonState(self)
        self.credits_state = CreditsState(self)
        self.current_state = self.main_menu_state

        self.audio_manager.play_music("menu")
        
        # Start the main game loop
        self.loop()

    def loop(self):
        while True:

            # DEBUG Print current state name
            state_name = self.current_state.__class__.__name__
            print(f"Current State: {state_name}")

            action = self.current_state.handle_input()
            if action == "new_game":
                self.game_state.new_game()
                self.game_state._update_dimensions()
                self.renderer.update_scaling()
                self.current_state = self.game_playing_state
                if self.audio_manager.sound_enabled:
                    self.audio_manager.play_music("level")

            elif action and action.startswith("start_level_"):
                level = int(action.split("_")[-1])
                if self.scores.is_level_unlocked(level):
                    self.game_state.start_level(level)
                    self.game_state._update_dimensions()
                    self.renderer.update_scaling()
                    self.current_state = self.game_playing_state
                    if self.audio_manager.sound_enabled:
                        self.audio_manager.play_music("level")
                else:
                    print("Level is locked!")

            elif action == "return_to_menu":
                if (self.game_state.total_score > 0 and 
                    self.scores.is_high_score(self.game_state.total_score)):
                    self.menu.name_entry_menu.score = self.game_state.total_score
                    self.current_state = self.name_entry_state
                else:
                    self.current_state = self.main_menu_state
                    self.audio_manager.play_music("menu")
            
            elif action == "level_won":
                self.current_state = self.level_won_state
            
            elif action == "game_completed":
                if (self.game_state.total_score > 0 and 
                    self.scores.is_high_score(self.game_state.total_score)):
                    self.menu.name_entry_menu.score = self.game_state.total_score
                    self.current_state = self.name_entry_state
                else:
                    self.current_state = self.game_won_state

            elif action == "next_level":
                self.current_state = self.game_playing_state

            self.current_state.draw()
