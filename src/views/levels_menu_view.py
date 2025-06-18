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
        self.level_rects = [] # Store level button positions for mouse interaction
        self.back_rect = None

    def draw(self):
        # Clear the screen
        self.display.fill((0, 0, 0))

        # Draw background image
        if self.background_image:
            self.display.blit(self.background_image, (0, 0))

        # Draw title
        title = self.menu_font.render("LEVELS", True, (255, 130, 0))
        title_rect = center_text(self.display, title, 100)
        self.display.blit(title, title_rect)
        
        # Create levels view background
        menu_width = 400
        menu_height = 420
        menu_x, menu_y = center_rect(self.display, menu_width, 200)
        self.draw_menu_background(menu_width, menu_height, menu_x, menu_y)

        # Draw levels in two columns
        for i in range(self.total_levels):
            col = i // self.levels_per_column
            row = i % self.levels_per_column
            
            # Set color based on level state
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
        self.back_rect = center_text(self.display, back_text, menu_y + menu_height - 35)
        self.back_rect = back_text.get_rect(topleft=(self.back_rect.x, self.back_rect.y))
        self.display.blit(back_text, self.back_rect)
