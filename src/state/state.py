class State:
    def __init__(self, sokonaut):
        self.sokonaut = sokonaut
        self.display = sokonaut.display

    def handle_input(self):
        pass

    def draw(self):
        pass

    def _return_to_menu(self):
        self.sokonaut.current_state = self.sokonaut.main_menu_state
        self.sokonaut.audio_manager.play_music("menu")
        return "return_to_menu"