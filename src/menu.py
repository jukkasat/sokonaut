import sys
import pygame

class Menu:
    def __init__(self, display, renderer):
        self.display = display
        self.renderer = renderer
        self.in_menu = True
        self.in_levels = False
        self.menu_font = pygame.font.SysFont("Arial", 74)
        self.menu_font_small = pygame.font.SysFont("Arial", 24)
        self.menu_items = ["New Game", "Levels", "High Score", "Quit"]
        self.selected_item = 0

        # Levels menu state
        self.levels_per_column = 11
        self.total_levels = 21
        self.selected_level = 0

    def draw(self):
        if self.in_levels:
            self.draw_levels()
        else:
            self.draw_main_menu()

    def draw_main_menu(self):
        self.display.fill((0, 0, 0))
        
        # Draw background first
        self.renderer.draw_menu_background()
        
        # Draw title
        title = self.menu_font.render("SOKONAUT", True, (224, 127, 50))
        title_pos = (self.display.get_width() // 2 - title.get_width() // 2, 100)
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
        
        pygame.display.flip()

    def draw_levels(self):
        self.display.fill((0, 0, 0))
        self.renderer.draw_menu_background()
        
        # Draw title
        title = self.menu_font.render("LEVELS", True, (224, 127, 50))
        title_pos = (self.display.get_width() // 2 - title.get_width() // 2, 100)
        self.display.blit(title, title_pos)
        
        # Create levels background
        menu_width = 400
        menu_height = 500
        menu_surface = pygame.Surface((menu_width, menu_height), pygame.SRCALPHA)
        
        pygame.draw.rect(
            menu_surface, 
            (50, 50, 50, 200),
            (0, 0, menu_width, menu_height),
            border_radius=15
        )
        
        menu_x = self.display.get_width() // 2 - menu_width // 2
        menu_y = 210
        self.display.blit(menu_surface, (menu_x, menu_y))
        
        # Draw level numbers in two columns
        for i in range(self.total_levels):
            col = i // self.levels_per_column
            row = i % self.levels_per_column
            
            color = (210, 105, 30) if i == self.selected_level else (200, 200, 200)
            text = self.menu_font_small.render(f"Level {i + 1}", True, color)
            
            x = menu_x + 50 + (col * 200)
            y = menu_y + 30 + (row * 40)
            self.display.blit(text, (x, y))
        
        # Draw back instruction
        back_text = self.menu_font_small.render("Press ESC to return", True, (200, 200, 200))
        back_x = self.display.get_width() // 2 - back_text.get_width() // 2
        back_y = menu_y + menu_height + 20
        self.display.blit(back_text, (back_x, back_y))
        
        pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if self.in_levels:
                    return self.handle_levels_input(event)
                else:
                    return self.handle_main_menu_input(event)
        return None

    def handle_main_menu_input(self, event):
        if event.key == pygame.K_UP:
            self.selected_item = (self.selected_item - 1) % len(self.menu_items)
        elif event.key == pygame.K_DOWN:
            self.selected_item = (self.selected_item + 1) % len(self.menu_items)
        elif event.key == pygame.K_RETURN:
            return self.handle_selection()
        return None

    def handle_levels_input(self, event):
        if event.key == pygame.K_ESCAPE:
            self.in_levels = False
        elif event.key == pygame.K_UP:
            self.selected_level = max(0, self.selected_level - 1)
        elif event.key == pygame.K_DOWN:
            self.selected_level = min(self.total_levels - 1, self.selected_level + 1)
        elif event.key == pygame.K_LEFT:
            self.selected_level = max(0, self.selected_level - self.levels_per_column)
        elif event.key == pygame.K_RIGHT:
            self.selected_level = min(self.total_levels - 1, self.selected_level + self.levels_per_column)
        elif event.key == pygame.K_RETURN:
            # TODO: Implement level selection
            pass
        return None

    def handle_selection(self):
        selected = self.menu_items[self.selected_item]
        if selected == "New Game":
            return "new_game"
        elif selected == "Levels":
            self.in_levels = True
        elif selected == "Quit":
            pygame.quit()
            sys.exit()
        return None