import pygame
from game_state import GameState
from renderer import Renderer
from input_handler import InputHandler
from menu import Menu
from high_scores import HighScores

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
        self.high_scores = HighScores()
        self.menu = Menu(self.display, self.renderer, self.high_scores)

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
                    self.menu.in_menu = False
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
                    # Check for high score before returning to menu
                    if (self.game_state.total_score > 0 and 
                        self.high_scores.is_high_score(self.game_state.total_score)):
                        self.menu.entering_name = True
                        self.menu.current_name = ""
                        while self.menu.entering_name:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_RETURN and self.menu.current_name:
                                        self.high_scores.add_score(
                                            self.menu.current_name,
                                            self.game_state.total_score
                                        )
                                        self.menu.entering_name = False
                                    elif event.key == pygame.K_BACKSPACE:
                                        self.menu.current_name = self.menu.current_name[:-1]
                                    elif event.key == pygame.K_ESCAPE:
                                        self.menu.entering_name = False
                                    elif len(self.menu.current_name) < 15:
                                        if event.unicode.isalnum():
                                            self.menu.current_name += event.unicode
                            self.menu.draw_name_entry(self.game_state.total_score)
                    self.menu.in_menu = True
                self.renderer.draw()

# Entry point for the game
if __name__ == "__main__":
    Sokonaut()
