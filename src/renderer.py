
import pygame

class Renderer:
    def __init__(self, game_state, display):
        self.game_state = game_state
        self.display = display
        self.images = self.load_images()

        # Calculate scaling to fit screen width
        self.scale_factor = self.display.get_width() / (self.game_state.width * self.images[0].get_width())
        self.tile_size = int(self.images[0].get_width() * self.scale_factor)
        
        # Calculate centering offsets
        self.offset_x = 0  # Will be 0 when scaling to full width
        self.offset_y = (self.display.get_height() - (self.game_state.height * self.tile_size)) // 2
        
        # Scale all images
        self.scaled_images = []
        for image in self.images:
            scaled = pygame.transform.scale(image, (self.tile_size, self.tile_size))
            self.scaled_images.append(scaled)

        self.menu_bg_width = self.display.get_width() // self.tile_size
        self.menu_bg_height = self.display.get_height() // self.tile_size

        self.font = pygame.font.SysFont("Arial", 24)

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

    def draw_menu_background(self):
        # Draw floor tiles
        for y in range(self.menu_bg_height):
            for x in range(self.menu_bg_width):
                # Draw walls on edges
                if x == 0 or x == self.menu_bg_width - 1 or y == 0 or y == self.menu_bg_height - 1:
                    tile = self.scaled_images[1]  # Wall
                else:
                    tile = self.scaled_images[0]  # Floor
                self.display.blit(tile, (x * self.tile_size, y * self.tile_size))

    def draw(self):
        self.display.fill((0, 0, 0))

        # Draw the game tiles with scaling and centering
        for y in range(self.game_state.height):
            for x in range(self.game_state.width):
                tile = self.game_state.map[y][x]
                pos_x = self.offset_x + (x * self.tile_size)
                pos_y = self.offset_y + (y * self.tile_size)
                self.display.blit(self.scaled_images[tile], (pos_x, pos_y))

        # Draw UI elements below the game field
        ui_y = self.offset_y + (self.game_state.height * self.tile_size) + 10
        
        # Display the move counter and game instructions
        text = self.font.render(f"Moves: {self.game_state.moves}", True, (255, 0, 0))
        self.display.blit(text, (25, ui_y))

        text = self.font.render("F2 = New Game", True, (255, 0, 0))
        self.display.blit(text, (200, ui_y))

        text = self.font.render("F3 = Restart Level", True, (255, 0, 0))
        self.display.blit(text, (400, ui_y))

        text = self.font.render("Esc = Close game", True, (255, 0, 0))
        self.display.blit(text, (620, ui_y))


        # Check if all levels are completed
        if self.game_state.game_completed():
            text = self.font.render("Game Won!", True, (255, 0, 0))
            text_x = self.tile_size * self.game_state.width / 2 - text.get_width() / 2  # Changed from self.scale
            text_y = self.tile_size * self.game_state.height / 2 - text.get_height() / 2  # Changed from self.scale
            pygame.draw.rect(self.display, (0, 0, 0), (text_x, text_y, text.get_width(), text.get_height()))
            self.display.blit(text, (text_x, text_y))

            # Show restart and quit options
            restart_text = self.font.render("Press F2 to Play Again", True, (255, 0, 0))
            restart_x = self.tile_size * self.game_state.width / 2 - restart_text.get_width() / 2  # Changed from self.scale
            restart_y = text_y + text.get_height() + 10
            pygame.draw.rect(self.display, (0, 0, 0), (restart_x, restart_y, restart_text.get_width(), restart_text.get_height()))
            self.display.blit(restart_text, (restart_x, restart_y))

            quit_text = self.font.render("Press ESC to Quit", True, (255, 0, 0))
            quit_x = self.tile_size * self.game_state.width / 2 - quit_text.get_width() / 2  # Changed from self.scale
            quit_y = restart_y + restart_text.get_height() + 10
            pygame.draw.rect(self.display, (0, 0, 0), (quit_x, quit_y, quit_text.get_width(), quit_text.get_height()))
            self.display.blit(quit_text, (quit_x, quit_y))
        
        # Check if level is completed
        elif self.game_state.level_won():
            text = self.font.render("Congrats, level won!", True, (255, 0, 0))
            text_x = self.tile_size * self.game_state.width / 2 - text.get_width() / 2
            text_y = self.tile_size * self.game_state.height / 2 - text.get_height() / 2
            pygame.draw.rect(self.display, (0, 0, 0), (text_x, text_y, text.get_width(), text.get_height()))
            self.display.blit(text, (text_x, text_y))

            # Add Next Level-button if not on last level
            if self.game_state.current_level < len(self.game_state.maps) - 1:
                next_text = self.font.render("Press SPACE for next level", True, (255, 0, 0))
                next_x = self.tile_size * self.game_state.width / 2 - next_text.get_width() / 2
                next_y = text_y + text.get_height() + 10
                pygame.draw.rect(self.display, (0, 0, 0), (next_x, next_y, next_text.get_width(), next_text.get_height()))
                self.display.blit(next_text, (next_x, next_y))

        pygame.display.flip()
