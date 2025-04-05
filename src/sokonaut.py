
import pygame
from game_state import GameState
from renderer import Renderer
from input_handler import InputHandler

class Sokonaut:

    def __init__(self):
        pygame.init()
        self.game_state = GameState()
        self.renderer = Renderer(self.game_state)
        self.input_handler = InputHandler(self.game_state)
        self.loop()

    def loop(self):
        while True:
            self.input_handler.handle_events()
            self.renderer.draw()

# Entry point for the game
if __name__ == "__main__":
    Sokonaut()
