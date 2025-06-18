from src.state.state import State

class MenuState(State):
    def __init__(self, sokonaut):
        super().__init__(sokonaut)
        self.in_menu = True

    def _return_to_menu(self):
        self.sokonaut.audio_manager.play_sound("select")
        self.sokonaut.current_state = self.sokonaut.main_menu_state