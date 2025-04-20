
import pygame

class Renderer:
    def __init__(self, game_state, display):
        self.game_state = game_state
        self.display = display
        self.images = self.load_images()
        self.level_backgrounds = self.load_level_backgrounds()
        self.game_won_background = self.load_game_won_background()

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
        for name in ["floor1", "wall1", "target1", "barrel1", "player3", "ready1", "robotarget1"]:
            try:
                image = pygame.image.load("src/img/" + name + ".png")
                images.append(image)
            except pygame.error as e:
                print(f"Warning: Could not load image '{name}'. Error: {e}")
                images.append(None)  # Append None to maintain index consistency
    
        if not images:
            raise RuntimeError("No images were loaded. Ensure the image files exist in 'src/img/'.")
        
        return images
    
    def load_level_backgrounds(self):
        level_backgrounds = []
        for i in range(0, 6):  # Load level_background0.png to level_background6.png
            try:
                background_image = pygame.image.load(f"src/img/level_background{i}.png")
                level_backgrounds.append(pygame.transform.scale(background_image, (self.display.get_width(), self.display.get_height())))
            except pygame.error as e:
                print(f"Warning: Could not load level background image {i}. Error: {e}")
                level_backgrounds.append(None)
        return level_backgrounds
    
    def load_game_won_background(self):
        try:
            background_image = pygame.image.load("src/img/game_won_background.png")
            return pygame.transform.scale(background_image, (self.display.get_width(), self.display.get_height()))
        except pygame.error as e:
            print(f"Warning: Could not load level won background image. Error: {e}")
            return None

    def draw(self):
        # Update scaling before drawing in case map dimensions changed
        self.update_scaling()
        self.display.fill((0, 0, 0))

       # Determine which background image to use based on the level
        background_index = None
        if self.game_state.current_level == 0:
            background_index = 0
        elif 1 <= self.game_state.current_level <= 5:
            background_index = 1
        elif 6 <= self.game_state.current_level <= 10:
            background_index = 2
        elif 11 <= self.game_state.current_level <= 15:
            background_index = 3
        elif 16 <= self.game_state.current_level <= 20:
            background_index = 4
        elif self.game_state.current_level == 21:
            background_index = 5

        # Draw level background image
        if (background_index is not None and
            background_index < len(self.level_backgrounds) and
            self.level_backgrounds[background_index]):
            self.display.blit(self.level_backgrounds[background_index], (0, 0))

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


        # Draw semi-transparent strip at the bottom
        strip_height = 40  # Height of the strip
        strip = pygame.Surface((self.display.get_width(), strip_height), pygame.SRCALPHA)
        strip.fill((0, 0, 0, 188))  # Black with 50% transparency
        self.display.blit(strip, (0, self.display.get_height() - strip_height))


        # Draw UI elements below the game field
        # ui_y = self.offset_y + (self.game_state.height * self.tile_size) + 10
        ui_y = self.display.get_height() - 35  # Position 35 pixels from the bottom
        
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
            # Draw level won background
            if self.game_won_background:
                self.display.blit(self.game_won_background, (0, 0))

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
            text = self.font.render(f"SCORE: {self.game_state.level_score}", True, (200, 200, 200))
            score_x = self.display.get_width() // 2 - text.get_width() // 2
            score_y = menu_y + 80
            self.display.blit(text, (score_x, score_y))

            # Add Next Level-button if not on last level
            if self.game_state.current_level < len(self.game_state.maps) - 1:
                next_text = self.font.render("Press ENTER to start next level", True, (200, 200, 200))
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
