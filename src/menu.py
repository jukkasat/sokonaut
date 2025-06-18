from src.views.main_menu_view import MainMenu
from src.views.levels_menu_view import LevelsMenu
from src.views.high_score_view import HighScoresView
from src.views.name_entry_view import NameEntryView
from src.views.credits_menu_view import CreditsMenu

class Menu:
    def __init__(self, display, renderer, scores):
        self.display = display
        self.renderer = renderer
        self.scores = scores
        self.main_menu = MainMenu(display, renderer, scores)
        self.levels_menu = LevelsMenu(display, renderer, scores)
        self.high_scores_view = HighScoresView(display, renderer, scores)
        self.name_entry_view = NameEntryView(display, renderer, scores)
        self.credits_menu = CreditsMenu(display, renderer, scores)
