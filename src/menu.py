import pygame
from src.views.main_menu_view import MainMenu
from src.views.levels_menu_view import LevelsMenu
from src.views.high_score_view import HighScoresMenu
from src.views.name_entry_view import NameEntryMenu

class Menu:
    def __init__(self, display, renderer, scores=None, audio_manager=None):
        self.display = display
        self.renderer = renderer
        self.scores = scores
        self.audio_manager = audio_manager
        self.in_menu = True
        self.active_menu = "main_menu"  # Start with the main menu
        self.current_name = ""

        self.main_menu = MainMenu(display, renderer, scores)
        self.levels_menu = LevelsMenu(display, renderer, scores)
        self.high_scores_menu = HighScoresMenu(display, renderer, scores)
        self.name_entry_menu = NameEntryMenu(display, renderer, scores)

    def draw(self):
        if self.active_menu == "main_menu":
            self.main_menu.draw()
        elif self.active_menu == "levels":
            self.levels_menu.draw()
        elif self.active_menu == "high_score":
            self.high_scores_menu.draw()
        elif self.active_menu == "name_entry":
            self.name_entry_menu.draw()

    def handle_input(self):
        # Handle user input events
        event = pygame.event.wait()
        if self.active_menu == "main_menu":
            action = self.main_menu.handle_input(event)
            if action == "new_game":
                self.audio_manager.play_sound("select")
                return "new_game"
            elif action == "levels":
                self.audio_manager.play_sound("select")
                self.active_menu = "levels"
                return None
            elif action == "high_score":
                self.audio_manager.play_sound("select")
                self.active_menu = "high_score"
                return None
            elif action is not None:
                self.audio_manager.play_sound("select")
                return action
        elif self.active_menu == "levels":
            action = self.levels_menu.handle_input(event)
            if action == "main_menu":
                self.audio_manager.play_sound("select")
                self.active_menu = "main_menu"
                return None
            elif action is not None:
                self.audio_manager.play_sound("select")
                return action
        elif self.active_menu == "high_score":
            action = self.high_scores_menu.handle_input(event)
            if action == "main_menu":
                self.audio_manager.play_sound("select")
                self.active_menu = "main_menu"
                return None
        return None
