import pygame
import sys
from src.views.menu_base import MenuBase
from src.utils.helper import center_text, center_rect

class MainMenu(MenuBase):
    def __init__(self, display, renderer, scores, audio_manager):
        super().__init__(display, renderer, scores)
        self.menu_items = ["New Game", "Levels", "High Score", "Quit"]
        self.selected_item = 0
        self.background_image = self.load_menu_background()
        self.audio_manager = audio_manager
        
    def draw(self):
        # Clear the screen
        self.display.fill((0, 0, 0))

        # Draw background image
        if self.background_image:
            self.display.blit(self.background_image, (0, 0))

        # Draw title
        title = self.menu_font.render("SOKONAUT", True, (255, 130, 0))
        title_rect = center_text(self.display, title, 80)
        self.display.blit(title, title_rect)
        
        # Create a surface for the menu background with alpha channel
        menu_width = 300  # Width of the menu background
        menu_height = len(self.menu_items) * 50 + 80  # Height based on items plus padding
        menu_x = self.display.get_width() // 2 - menu_width // 2
        menu_y = 210  # Adjust this value to position the menu box
        self.draw_menu_background(menu_width, menu_height, menu_x, menu_y)

        # Store menu item positions for mouse interaction
        self.menu_item_rects = []
        # Draw menu items
        for i, item in enumerate(self.menu_items):
            color = (210, 105, 30) if i == self.selected_item else (200, 200, 200)
            text = self.menu_font_small.render(item, True, color)
            pos = (self.display.get_width() // 2 - text.get_width() // 2, 250 + i * 50)
            self.menu_item_rects.append(text.get_rect(topleft=pos))
            self.display.blit(text, pos)
        
        # Update the display
        pygame.display.flip()

    def handle_input(self, event):
        # Handle input for the main menu
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_item = (self.selected_item - 1) % len(self.menu_items)
                self.audio_manager.play_sound("menu_select")
            elif event.key == pygame.K_DOWN:
                self.selected_item = (self.selected_item + 1) % len(self.menu_items)
                self.audio_manager.play_sound("menu_select")
            elif event.key == pygame.K_RETURN:
                return self.handle_selection()
            
        # Handle mouse input
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            for i, rect in enumerate(self.menu_item_rects):
                if rect.collidepoint(mouse_pos):
                    if self.selected_item != i:
                        self.selected_item = i
                        self.audio_manager.play_sound("menu_select")
                    break
                    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                mouse_pos = pygame.mouse.get_pos()
                for i, rect in enumerate(self.menu_item_rects):
                    if rect.collidepoint(mouse_pos):
                        self.selected_item = i
                        return self.handle_selection()
        return None

    def handle_selection(self):
        # Handle selection in the main menu
        selected = self.menu_items[self.selected_item]
        if selected == "New Game":
            return "new_game"
        elif selected == "Levels":
            return "levels"
        elif selected == "High Score":
            return "high_score"
        elif selected == "Quit":
            pygame.quit()
            sys.exit()
        return None