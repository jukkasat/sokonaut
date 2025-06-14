from src.views.main_menu_view import MainMenu
from src.views.levels_menu_view import LevelsMenu
from src.views.high_score_view import HighScoresMenu
from src.views.name_entry_view import NameEntryMenu

class Menu:
    def __init__(self, display, renderer, scores, audio_manager):
        self.display = display
        self.renderer = renderer
        self.scores = scores
        self.audio_manager = audio_manager
        self.main_menu = MainMenu(display, renderer, scores, audio_manager)
        self.levels_menu = LevelsMenu(display, renderer, scores, audio_manager)
        self.high_scores_menu = HighScoresMenu(display, renderer, scores)
        self.name_entry_menu = NameEntryMenu(display, renderer, scores)
