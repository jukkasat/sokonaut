from src.state.state import State

class MenuState(State):
    def __init__(self, sokonaut):
        super().__init__(sokonaut)
        self.in_menu = True

    def handle_input(self):
        pass

    def draw(self):
        pass