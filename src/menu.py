import sys
import pygame

class Menu:
    def __init__(self, display, renderer, high_scores=None):
        # Initialize menu state and attributes
        self.display = display
        self.renderer = renderer
        self.high_scores = high_scores
        self.in_menu = True
        self.in_levels = False
        self.menu_font = pygame.font.SysFont("Arial", 74)
        self.menu_font_small = pygame.font.SysFont("Arial", 20)
        self.menu_items = ["New Game", "Levels", "High Score", "Quit"]
        self.selected_item = 0
        self.tile_size = 32  # Fixed tile size for walls

        # Levels menu state
        self.levels_per_column = 11
        self.total_levels = 22
        self.selected_level = 0

        # High score states
        self.in_high_scores = False
        self.entering_name = False
        self.current_name = ""

        self.wall_image = pygame.transform.scale(
            renderer.images[1], # Wall tile is index 0
            (self.tile_size, self.tile_size)
        )
        self.floor_image = pygame.transform.scale(
            renderer.images[0],  # Floor tile is index 0
            (self.tile_size, self.tile_size)
        )
        self.box_image = pygame.transform.scale(
            renderer.images[3],  # Box tile is index 3
            (self.tile_size, self.tile_size)
        )
        self.target_image = pygame.transform.scale(
            renderer.images[2],  # Target tile is index 2
            (self.tile_size, self.tile_size)
        )

    def draw(self):
        # Draw the appropriate menu based on the current state
        if self.in_levels:
            self.draw_levels()
        elif self.in_high_scores:
            self.draw_high_scores()
        else:
            self.draw_main_menu()

    def draw_main_menu(self):
        # Clear the screen
        self.display.fill((0, 0, 0))

        # Draw background
        self.draw_background()

        # Draw title
        title = self.menu_font.render("SOKONAUT", True, (224, 127, 50))
        title_pos = (self.display.get_width() // 2 - title.get_width() // 2, 80)
        self.display.blit(title, title_pos)
        
        # Create a surface for the menu background with alpha channel
        menu_width = 300  # Width of the menu background
        menu_height = len(self.menu_items) * 50 + 80  # Height based on items plus padding
        menu_surface = pygame.Surface((menu_width, menu_height), pygame.SRCALPHA)
        
        # Draw rounded rectangle with alpha
        pygame.draw.rect(
            menu_surface, 
            (50, 50, 50, 200),  # RGBA: white with 50% transparency
            (0, 0, menu_width, menu_height),
            border_radius=15
        )
        
        # Position the menu background
        menu_x = self.display.get_width() // 2 - menu_width // 2
        menu_y = 210  # Adjust this value to position the menu box
        self.display.blit(menu_surface, (menu_x, menu_y))
        
        # Draw menu items
        for i, item in enumerate(self.menu_items):
            color = (210, 105, 30) if i == self.selected_item else (200, 200, 200)
            text = self.menu_font_small.render(item, True, color)
            pos = (self.display.get_width() // 2 - text.get_width() // 2, 250 + i * 50)
            self.display.blit(text, pos)
        
        # Update the display
        pygame.display.flip()

    def draw_levels(self):
        # Clear the screen
        self.display.fill((0, 0, 0))

        # Draw background
        self.draw_background()

        # Draw title
        title = self.menu_font.render("LEVELS", True, (224, 127, 50))
        title_pos = (self.display.get_width() // 2 - title.get_width() // 2, 80)
        self.display.blit(title, title_pos)
        
        # Create levels view background
        menu_width = 400
        menu_height = 420
        menu_surface = pygame.Surface((menu_width, menu_height), pygame.SRCALPHA)
        
        # Draw rounded rectangle for levels menu
        pygame.draw.rect(
            menu_surface, 
            (50, 50, 50, 200),
            (0, 0, menu_width, menu_height),
            border_radius=15
        )
        
        # Position the levels menu background
        menu_x = self.display.get_width() // 2 - menu_width // 2
        menu_y = 200
        self.display.blit(menu_surface, (menu_x, menu_y))
        
        # Draw levels in two columns
        for i in range(self.total_levels):
            col = i // self.levels_per_column  # Split into two columns
            row = i % self.levels_per_column
            
            color = (210, 105, 30) if i == self.selected_level else (200, 200, 200)
            text = self.menu_font_small.render(f"Level {i}", True, color)
            
            x = menu_x + 50 + (col * 200)
            y = menu_y + 30 + (row * 30)  # 30 pixels between levels
            self.display.blit(text, (x, y))
            
        # Draw back button
        back_text = self.menu_font_small.render("BACK", True, 
                                            (210, 105, 30) if self.selected_level == -1 else (200, 200, 200))
        back_x = self.display.get_width() // 2 - back_text.get_width() // 2
        back_y = menu_y + menu_height - 45  # Position back button near bottom of menu box
        self.display.blit(back_text, (back_x, back_y))
        
        # Update the display
        pygame.display.flip()

    def draw_high_scores(self):
        self.display.fill((0, 0, 0))

        # Draw background
        self.draw_background()

        # Draw title
        title = self.menu_font.render("HIGH SCORES", True, (224, 127, 50))
        title_pos = (self.display.get_width() // 2 - title.get_width() // 2, 80)
        self.display.blit(title, title_pos)

        # Create background for scores
        menu_width = 400
        menu_height = 490
        menu_surface = pygame.Surface((menu_width, menu_height), pygame.SRCALPHA)
        pygame.draw.rect(menu_surface, (50, 50, 50, 200), (0, 0, menu_width, menu_height), border_radius=15)
        
        menu_x = self.display.get_width() // 2 - menu_width // 2
        menu_y = 180
        self.display.blit(menu_surface, (menu_x, menu_y))

        # Draw scores
        y_pos = menu_y + 40
        if self.high_scores is not None:
            for i, score in enumerate(self.high_scores.get_scores()):
                rank_text = self.menu_font_small.render(f"{i+1}.", True, (200, 200, 200))
                name_text = self.menu_font_small.render(score["name"], True, (200, 200, 200))
                score_text = self.menu_font_small.render(str(score["score"]), True, (200, 200, 200))
                
                self.display.blit(rank_text, (menu_x + 50, y_pos))
                self.display.blit(name_text, (menu_x + 100, y_pos))
                self.display.blit(score_text, (menu_x + 300, y_pos))
                y_pos += 40
            y_pos += 40

        # Draw back text
        back_text = self.menu_font_small.render("Press ESC to return", True, (200, 200, 200))
        back_x = self.display.get_width() // 2 - back_text.get_width() // 2
        back_y = menu_y + menu_height - 40
        self.display.blit(back_text, (back_x, back_y))

        pygame.display.flip()

    def draw_name_entry(self, score):
        # Create name entry box
        menu_width = 400
        menu_height = 200
        menu_surface = pygame.Surface((menu_width, menu_height), pygame.SRCALPHA)
        pygame.draw.rect(menu_surface, (50, 50, 50, 200), (0, 0, menu_width, menu_height), border_radius=15)
        
        menu_x = self.display.get_width() // 2 - menu_width // 2
        menu_y = self.display.get_height() // 2 - menu_height // 2
        self.display.blit(menu_surface, (menu_x, menu_y))

        # Draw text
        text = self.menu_font_small.render("New High Score!", True, (210, 105, 30))
        score_text = self.menu_font_small.render(f"Score: {score}", True, (200, 200, 200))
        name_text = self.menu_font_small.render("Enter your name:", True, (200, 200, 200))
        input_text = self.menu_font_small.render(self.current_name + "_", True, (200, 200, 200))
        
        text_x = self.display.get_width() // 2 - text.get_width() // 2
        self.display.blit(text, (text_x, menu_y + 30))
        self.display.blit(score_text, (text_x, menu_y + 60))
        self.display.blit(name_text, (text_x, menu_y + 90))
        self.display.blit(input_text, (text_x, menu_y + 120))

        pygame.display.flip()

    def draw_background(self):
        # Draw floor tiles
        for y in range(0, self.display.get_height(), self.tile_size):
            for x in range(0, self.display.get_width(), self.tile_size):
                self.display.blit(self.floor_image, (x, y))

        # Draw walls around the screen using scaled wall tiles
        for x in range(0, self.display.get_width(), self.tile_size):
            self.display.blit(self.wall_image, (x, 0))  # Top wall
            self.display.blit(self.wall_image, (x, self.display.get_height() - self.tile_size))  # Bottom wall
        
        for y in range(0, self.display.get_height(), self.tile_size):  # Adjust vertical range
            self.display.blit(self.wall_image, (0, y))  # Left wall
            self.display.blit(self.wall_image, (self.display.get_width() - self.tile_size, y))  # Right wall
        
        # Draw some decorative boxes and targets
        decorative_elements = [
            (5, 5, 'target'), (5, 6, 'box'),
            (10, 11, 'box'), (10, 12, 'target'),
            (8, 16, 'target'), (9, 16, 'box'),
            (30, 15, 'box'), (31, 15, 'target'),
            (32, 6, 'target'), (32, 7, 'box')
        ]
        for x_tile, y_tile, elem_type in decorative_elements:
            x = x_tile * self.tile_size
            y = y_tile * self.tile_size
            if elem_type == 'box':
                self.display.blit(self.box_image, (x, y))
            else:
                self.display.blit(self.target_image, (x, y))

    def handle_input(self):
        # Handle user input events
        while self.in_high_scores or self.in_menu or self.in_levels or self.entering_name:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.entering_name:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.current_name = self.current_name[:-1]
                        elif event.key == pygame.K_RETURN:
                            self.entering_name = False
                            return self.current_name
                        else:
                            self.current_name += event.unicode
                    continue
                    return
                    
                if event.type == pygame.KEYDOWN:
                    if self.in_levels:
                        return self.handle_levels_input(event)
                    elif self.in_high_scores:
                        if event.key == pygame.K_ESCAPE:
                            self.in_high_scores = False
                            return None
                    else:
                        return self.handle_main_menu_input(event)

                
            # Draw current menu state
            if self.in_high_scores:
                self.draw_high_scores()
            elif self.in_levels:
                self.draw_levels()
            else:
                self.draw_main_menu()
        return None

    def handle_main_menu_input(self, event):
        # Handle input for the main menu
        if event.key == pygame.K_UP:
            self.selected_item = (self.selected_item - 1) % len(self.menu_items)
        elif event.key == pygame.K_DOWN:
            self.selected_item = (self.selected_item + 1) % len(self.menu_items)
        elif event.key == pygame.K_RETURN:
            return self.handle_selection()
        return None

    def handle_levels_input(self, event):
        # Handle input for the levels menu
        if event.key == pygame.K_ESCAPE:
            self.in_levels = False
        elif event.key == pygame.K_UP:
            if self.selected_level == -1:  # If on back button
                self.selected_level = self.total_levels - 1
            else:
                self.selected_level = (self.selected_level - 1) % (self.total_levels + 1)
                if self.selected_level == self.total_levels:
                    self.selected_level = -1  # Move to back button
        elif event.key == pygame.K_DOWN:
            if self.selected_level == -1:  # If on back button
                self.selected_level = 0
            else:
                self.selected_level = (self.selected_level + 1) % (self.total_levels + 1)
                if self.selected_level == self.total_levels:
                    self.selected_level = -1  # Move to back button
        elif event.key == pygame.K_RETURN:
            if self.selected_level == -1:  # Back button selected
                self.in_levels = False
            else:
                self.in_levels = False
                self.in_menu = False
                return f"start_level_{self.selected_level}"
        return None
    
    def handle_selection(self):
        # Handle selection in the main menu
        selected = self.menu_items[self.selected_item]
        if selected == "New Game":
            return "new_game"
        elif selected == "Levels":
            self.in_levels = True
            self.selected_level = 0
        elif selected == "High Score":
            if self.high_scores:
                self.in_high_scores = True
                self.draw_high_scores()
        elif selected == "Quit":
            pygame.quit()
            sys.exit()
        return None
