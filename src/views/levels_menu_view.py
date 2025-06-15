import pygame
from src.views.menu_base import MenuBase
from src.utils.helper import center_text, center_rect

class LevelsMenu(MenuBase):
    def __init__(self, display, renderer, scores, audio_manager):
        super().__init__(display, renderer, scores)
        self.levels_per_column = 11
        self.total_levels = 22
        self.selected_level = 0
        self.background_image = self.load_menu_background()
        self.audio_manager = audio_manager

    def draw(self):
        # Clear the screen
        self.display.fill((0, 0, 0))

        # Draw background image
        if self.background_image:
            self.display.blit(self.background_image, (0, 0))

        # Draw title
        title = self.menu_font.render("LEVELS", True, (255, 130, 0))
        title_rect = center_text(self.display, title, 80)
        self.display.blit(title, title_rect)
        
        # Create levels view background
        menu_width = 400
        menu_height = 420
        menu_x, menu_y = center_rect(self.display, menu_width, 200)
        self.draw_menu_background(menu_width, menu_height, menu_x, menu_y)
        
        # Draw levels in two columns
        for i in range(self.total_levels):
            col = i // self.levels_per_column  # Split into two columns
            row = i % self.levels_per_column
            
            if self.scores.is_level_unlocked(i):
                color = (210, 105, 30) if i == self.selected_level else (200, 200, 200)
            else:
                color = (200, 105, 30) if i == self.selected_level else (100, 100, 100)  # Gray color for locked levels
            text = self.menu_font_small.render(f"Level {i}", True, color)
            
            x = menu_x + 50 + (col * 200)
            y = menu_y + 30 + (row * 30)  # 30 pixels between levels
            self.display.blit(text, (x, y))
        
        # Store level button positions for mouse interaction
        self.level_rects = []
        # Draw levels in two columns
        for i in range(self.total_levels):
            col = i // self.levels_per_column
            row = i % self.levels_per_column
            
            if self.scores.is_level_unlocked(i):
                color = (210, 105, 30) if i == self.selected_level else (200, 200, 200)
            else:
                color = (200, 105, 30) if i == self.selected_level else (100, 100, 100)
            text = self.menu_font_small.render(f"Level {i}", True, color)
            
            x = menu_x + 50 + (col * 200)
            y = menu_y + 30 + (row * 30)
            self.level_rects.append((pygame.Rect(x, y, text.get_width(), text.get_height()), i))
            self.display.blit(text, (x, y))
    
        # Draw and store back button position
        back_text = self.menu_font_small.render("BACK", True, (210, 105, 30) if self.selected_level == -1 else (200, 200, 200))
        back_rect = center_text(self.display, back_text, menu_y + menu_height - 45)
        self.back_rect = back_text.get_rect(topleft=(back_rect.x, back_rect.y))
        self.display.blit(back_text, back_rect)

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
                self.audio_manager.play_sound("level_select")
            elif event.key == pygame.K_DOWN:
                if self.selected_level == -1:  # If on back button
                    self.selected_level = 0
                else:
                    self.selected_level = (self.selected_level + 1) % (self.total_levels + 1)
                    if self.selected_level == self.total_levels:
                        self.selected_level = -1  # Move to back button
                self.audio_manager.play_sound("level_select")
            elif event.key == pygame.K_RETURN:
                if self.selected_level == -1:  # Back button selected
                    return "main_menu"
                else:
                    if self.scores.is_level_unlocked(self.selected_level):
                        return f"start_level_{self.selected_level}"
                    else:
                        return None
                    
        # Handle mouse input
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            
            # Check level buttons
            old_selected = self.selected_level
            for rect, level in self.level_rects:
                if rect.collidepoint(mouse_pos):
                    self.selected_level = level
                    if old_selected != level:
                        self.audio_manager.play_sound("level_select")
                    break
            
            # Check back button
            if self.back_rect.collidepoint(mouse_pos):
                if self.selected_level != -1:
                    self.selected_level = -1
                    self.audio_manager.play_sound("level_select")
                
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                mouse_pos = pygame.mouse.get_pos()
                
                # Check level buttons
                for rect, level in self.level_rects:
                    if rect.collidepoint(mouse_pos):
                        if self.scores.is_level_unlocked(level):
                            return f"start_level_{level}"
                        break
                
                # Check back button
                if self.back_rect.collidepoint(mouse_pos):
                    return "main_menu"
        return None