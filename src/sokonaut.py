import pygame
from game_state import GameState
from renderer import Renderer
from input_handler import InputHandler
from menu import Menu

class Sokonaut:

    def __init__(self):
        # Initialize pygame and set up the game window
        pygame.init()
        self.screen_width = 1280
        self.screen_height = 720
        self.display = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Sokonaut")

        # Initialize game components
        self.game_state = GameState()  # Manages the game state
        self.renderer = Renderer(self.game_state, self.display)  # Handles rendering
        self.input_handler = InputHandler(self.game_state)  # Handles user input
        self.menu = Menu(self.display, self.renderer)  # Manages the menu

        # Start the main game loop
        self.loop()

    def loop(self):
        # Main game loop
        while True:
            if self.menu.in_menu:
                # Handle menu input and actions
                action = self.menu.handle_input()
                if action == "new_game":
                    self.game_state.new_game()
                    self.game_state._update_dimensions()
                    self.renderer.update_scaling()
                    self.menu.in_menu = False  # Exit menu and start the game
                elif action and action.startswith("start_level_"):
                    # Extract the level number from the action string
                    level = int(action.split("_")[-1])
                    # Set the current level in the game state
                    self.game_state.start_level(level)
                    # Update game dimensions based on the new level's map
                    self.game_state._update_dimensions()
                    # Update renderer scaling for new map
                    self.renderer.update_scaling()
                    # Exit the menu and start the game
                    self.menu.in_menu = False
                self.menu.draw()  # Draw the menu
            else:
                # Handle game input and rendering
                action = self.input_handler.handle_events()  # Get the action
                if action == "return_to_menu":
                    self.menu.in_menu = True  # Return to menu
                self.renderer.draw()

# Entry point for the game
if __name__ == "__main__":
    Sokonaut()
