
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
        images = []
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
        # Update scaling before drawing in case map dimensions changed
        self.update_scaling()
        self.display.fill((0, 0, 0))

        # Get current map dimensions
        map_width = len(self.game_state.map[0])
        map_height = len(self.game_state.map)

        # Draw the game tiles with scaling and centering
        for y in range(map_height):
            for x in range(map_width):
                tile = self.game_state.map[y][x]
                pos_x = self.offset_x + (x * self.tile_size)
                pos_y = self.offset_y + (y * self.tile_size)
                self.display.blit(self.scaled_images[tile], (pos_x, pos_y))

        # Draw UI elements below the game field
        ui_y = self.offset_y + (self.game_state.height * self.tile_size) + 10
        
        text = self.font.render(f"Level: {self.game_state.current_level}", True, (200, 200, 200))
        self.display.blit(text, (25, ui_y))
        
        text = self.font.render(f"Moves: {self.game_state.moves}", True, (210, 105, 30))
        self.display.blit(text, (150, ui_y))

        text = self.font.render(f"score: {self.game_state.total_score}", True, (200, 200, 200))
        self.display.blit(text, (self.display.get_width() // 2 - text.get_width() // 2, ui_y))

        text = self.font.render("F3 = Restart", True, (200, 200, 200))
        self.display.blit(text, (self.display.get_width() - text.get_width() - 170, ui_y))

        text = self.font.render("F2 = Menu", True, (200, 200, 200))
        self.display.blit(text, (self.display.get_width() - text.get_width() - 25, ui_y))


        # Check if all levels are completed
        if self.game_state.game_completed():
            # Create a semi-transparent background box for text
            menu_width = 400
            menu_height = 200
            menu_surface = pygame.Surface((menu_width, menu_height), pygame.SRCALPHA)
            
            # Draw rounded rectangle with alpha
            pygame.draw.rect(
                menu_surface, 
                (50, 50, 50, 216),  # Semi-transparent dark background
                (0, 0, menu_width, menu_height),
                border_radius=15
            )
            
            # Position the menu background in center
            menu_x = self.display.get_width() // 2 - menu_width // 2
            menu_y = self.display.get_height() // 2 - menu_height // 2
            self.display.blit(menu_surface, (menu_x, menu_y))

            # Draw game won text
            text = self.font.render("Game won, good job!", True, (210, 105, 30))
            text_x = self.display.get_width() // 2 - text.get_width() // 2
            text_y = menu_y + 30
            self.display.blit(text, (text_x, text_y))

            # Draw total score
            score_text = self.font.render(f"TOTAL SCORE: {self.game_state.total_score}", True, (200, 200, 200))
            score_x = self.display.get_width() // 2 - score_text.get_width() // 2
            score_y = menu_y + 90
            self.display.blit(score_text, (score_x, score_y))

            # Draw options text
            menu_text = self.font.render("F2 to Main menu", True, (200, 200, 200))
            menu_x = self.display.get_width() // 2 - menu_text.get_width() // 2
            menu_y = menu_y + 180
            self.display.blit(menu_text, (menu_x, menu_y - 30))
        
        # Check if level is completed
        elif self.game_state.level_won():         
            # Create a semi-transparent background box for text
            menu_width = 400
            menu_height = 180
            menu_surface = pygame.Surface((menu_width, menu_height), pygame.SRCALPHA)
            
            # Draw rounded rectangle with alpha
            pygame.draw.rect(
                menu_surface, 
                (50, 50, 50, 216),
                (0, 0, menu_width, menu_height),
                border_radius=15
            )
            
            # Position the menu background in center
            menu_x = self.display.get_width() // 2 - menu_width // 2
            menu_y = self.display.get_height() // 2 - menu_height // 2
            self.display.blit(menu_surface, (menu_x, menu_y))

            # Draw victory text
            text = self.font.render("Congrats, level won!", True, (210, 105, 30))
            text_x = self.display.get_width() // 2 - text.get_width() // 2
            text_y = menu_y + 30
            self.display.blit(text, (text_x, text_y))

            # Draw level score
            text = self.font.render(f"POINTS: {self.game_state.level_score}", True, (200, 200, 200))
            score_x = self.display.get_width() // 2 - text.get_width() // 2
            # score_y = text_y + text.get_height() + 20
            score_y = menu_y + 80
            self.display.blit(text, (score_x, score_y))

            # Add Next Level-button if not on last level
            if self.game_state.current_level < len(self.game_state.maps) - 1:
                next_text = self.font.render("Press SPACE for next level", True, (200, 200, 200))
                next_x = self.display.get_width() // 2 - next_text.get_width() // 2
                next_y = menu_y + 130
                self.display.blit(next_text, (next_x, next_y))

        pygame.display.flip()

    def update_scaling(self):
        """Update scaling factors when map dimensions change"""
        # Get current map dimensions
        map_width = len(self.game_state.map[0])
        map_height = len(self.game_state.map)
        
        # Calculate scaling to fit screen width and height
        width_scale = self.display.get_width() / (map_width * self.images[0].get_width())
        height_scale = (self.display.get_height() * 0.8) / (map_height * self.images[0].get_height())
        
        # Use the smaller scale to ensure the map fits both dimensions
        self.scale_factor = min(width_scale, height_scale)
        self.tile_size = int(self.images[0].get_width() * self.scale_factor)
        
        # Calculate centering offsets
        self.offset_x = (self.display.get_width() - (map_width * self.tile_size)) // 2
        self.offset_y = (self.display.get_height() - (map_height * self.tile_size)) // 2
        
        # Scale all images
        self.scaled_images = []
        for image in self.images:
            scaled = pygame.transform.scale(image, (self.tile_size, self.tile_size))
            self.scaled_images.append(scaled)
