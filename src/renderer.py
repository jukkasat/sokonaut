
import pygame

class Renderer:
    def __init__(self, game_state):
        self.game_state = game_state
        self.images = self.load_images()
        self.scale = self.images[0].get_width()
        self.display = self._init_display()
        self.font = pygame.font.SysFont("Arial", 24)

    def _init_display(self):
        display_height = self.scale * self.game_state.height
        display_width = self.scale * self.game_state.width
        return pygame.display.set_mode((display_width, display_height + self.scale))

    def load_images(self):
        # Load images for the game tiles
        images = []  # Create local images list
        for name in ["lattia", "seina", "kohde", "laatikko", "robo", "valmis", "kohderobo"]:
            try:
                image = pygame.image.load("src/img/" + name + ".png")
                images.append(image)
            except pygame.error as e:
                print(f"Warning: Could not load image '{name}'. Error: {e}")
                images.append(None)  # Append None to maintain index consistency
    
        if not images:
            raise RuntimeError("No images were loaded. Ensure the image files exist in 'src/img/'.")
        
        return images
    
    def draw(self):
        self.display.fill((0, 0, 0))

        # Draw the game tiles
        for y in range(self.game_state.height):
            for x in range(self.game_state.width):
                tile = self.game_state.map[y][x]
                self.display.blit(self.images[tile], (x * self.scale, y * self.scale))

        # Display the move counter and game instructions
        text = self.font.render(f"Moves: {self.game_state.moves}", True, (255, 0, 0))
        self.display.blit(text, (25, self.game_state.height * self.scale + 10))

        text = self.font.render("F2 = New Game", True, (255, 0, 0))
        self.display.blit(text, (200, self.game_state.height * self.scale + 10))

        text = self.font.render("F3 = Restart Level", True, (255, 0, 0))
        self.display.blit(text, (400, self.game_state.height * self.scale + 10))

        text = self.font.render("Esc = Close game", True, (255, 0, 0))
        self.display.blit(text, (400, self.game_state.height * self.scale + 10))

        # Check if all levels are completed
        if self.game_state.game_completed():
            text = self.font.render("Game Won!", True, (255, 0, 0))
            text_x = self.scale * self.game_state.width / 2 - text.get_width() / 2
            text_y = self.scale * self.game_state.height / 2 - text.get_height() / 2
            pygame.draw.rect(self.display, (0, 0, 0), (text_x, text_y, text.get_width(), text.get_height()))
            self.display.blit(text, (text_x, text_y))

            # Show restart and quit options
            restart_text = self.font.render("Press F2 to Play Again", True, (255, 0, 0))
            restart_x = self.scale * self.game_state.width / 2 - restart_text.get_width() / 2
            restart_y = text_y + text.get_height() + 10
            pygame.draw.rect(self.display, (0, 0, 0), (restart_x, restart_y, restart_text.get_width(), restart_text.get_height()))
            self.display.blit(restart_text, (restart_x, restart_y))

            quit_text = self.font.render("Press ESC to Quit", True, (255, 0, 0))
            quit_x = self.scale * self.game_state.width / 2 - quit_text.get_width() / 2
            quit_y = restart_y + restart_text.get_height() + 10
            pygame.draw.rect(self.display, (0, 0, 0), (quit_x, quit_y, quit_text.get_width(), quit_text.get_height()))
            self.display.blit(quit_text, (quit_x, quit_y))
        # Check if level is completed
        elif self.game_state.level_won():
            text = self.font.render("Congrats, level won!", True, (255, 0, 0))
            text_x = self.scale * self.game_state.width / 2 - text.get_width() / 2
            text_y = self.scale * self.game_state.height / 2 - text.get_height() / 2
            pygame.draw.rect(self.display, (0, 0, 0), (text_x, text_y, text.get_width(), text.get_height()))
            self.display.blit(text, (text_x, text_y))

            # Add Next Level-button if not on last level
            if self.game_state.current_level < len(self.game_state.maps) - 1:
                next_text = self.font.render("Press SPACE for next level", True, (255, 0, 0))
                next_x = self.scale * self.game_state.width / 2 - next_text.get_width() / 2
                next_y = text_y + text.get_height() + 10
                pygame.draw.rect(self.display, (0, 0, 0), (next_x, next_y, next_text.get_width(), next_text.get_height()))
                self.display.blit(next_text, (next_x, next_y))

        pygame.display.flip()
