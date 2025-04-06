
import pygame
from game_state import GameState
from renderer import Renderer
from input_handler import InputHandler
from menu import Menu

class Sokonaut:

    def __init__(self):
        pygame.init()
        self.screen_width = 1280
        self.screen_height = 720
        self.display = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Sokonaut")

        self.game_state = GameState()
        self.renderer = Renderer(self.game_state, self.display)
        self.input_handler = InputHandler(self.game_state)
        self.menu = Menu(self.display, self.renderer)

        self.loop()

    def loop(self):
        while True:
            if self.menu.in_menu:
                action = self.menu.handle_input()
                if action == "new_game":
                    self.menu.in_menu = False
                self.menu.draw()
            else:
                self.input_handler.handle_events()
                self.renderer.draw()

# Entry point for the game
if __name__ == "__main__":
    Sokonaut()
