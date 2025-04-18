import pygame
from views.menu_base import MenuBase

class LevelsMenu(MenuBase):
    def __init__(self, display, renderer, high_scores=None):
        super().__init__(display, renderer, high_scores)
        self.levels_per_column = 11
        self.total_levels = 22
        self.selected_level = 0

    def draw(self):
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

    def handle_input(self, event):
        # Handle input for the levels menu
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "main_menu"
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
                    return "main_menu"
                else:
                    return f"start_level_{self.selected_level}"
        return None