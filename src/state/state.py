class State:
    def __init__(self, sokonaut):
        self.sokonaut = sokonaut

    def _return_to_menu(self):
        """Check for high score and return appropriate action"""
        if (self.sokonaut.game_state.total_score > 0 and 
            self.sokonaut.scores.is_high_score(self.sokonaut.game_state.total_score)):
            self.sokonaut.menu.name_entry_menu.score = self.sokonaut.game_state.total_score
            self.sokonaut.current_state = self.sokonaut.name_entry_state
        else:
            self.sokonaut.current_state = self.sokonaut.main_menu_state
            self.sokonaut.audio_manager.play_music("menu")
