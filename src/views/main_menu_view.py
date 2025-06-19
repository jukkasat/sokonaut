import pygame
from src.views.menu_base import MenuBase
from src.utils.helper import center_text, get_base_path

class MainMenu(MenuBase):
    def __init__(self, display, renderer, scores):
        super().__init__(display, renderer, scores)
        self.menu_items = ["new game", "levels", "high score", "credits", "quit"]
        self.selected_item = 0
        self.background_image = self.load_menu_background()
        self.menu_font_small = pygame.font.SysFont("bahnschrift", 24)
        self.menu_item_rects = [] # Store menu item positions for mouse interaction
        self.music_icon_rect = None

        # Load music control icons
        try:
            self.audio_on_icon = pygame.image.load(get_base_path("img") + "/audio_on.png")
            self.audio_off_icon = pygame.image.load(get_base_path("img") + "/audio_off.png")
            icon_size = (74, 74)  # size
            self.audio_on_icon = pygame.transform.scale(self.audio_on_icon, icon_size)
            self.audio_off_icon = pygame.transform.scale(self.audio_off_icon, icon_size)
        except:
            print("Could not load music control icons")
            self.audio_on_icon = None
            self.audio_off_icon = None

    def draw(self):
        # Clear the screen
        self.display.fill((0, 0, 0))

        # Draw background image
        if self.background_image:
            self.display.blit(self.background_image, (0, 0))

        # Draw title
        title = self.menu_font.render("SOKONAUT", True, (255, 130, 0))
        title_rect = center_text(self.display, title, 100)
        self.display.blit(title, title_rect)
        
        # Create a surface for the menu background with alpha channel
        menu_width = 300  # Width of the menu background
        menu_height = len(self.menu_items) * 50 + 80  # Height based on items plus padding
        menu_x = self.display.get_width() // 2 - menu_width // 2
        menu_y = 210  # Adjust this value to position the menu box
        self.draw_menu_background(menu_width, menu_height, menu_x, menu_y)

        # Draw menu items
        for i, item in enumerate(self.menu_items):
            color = (210, 105, 30) if i == self.selected_item else (200, 200, 200)
            text = self.menu_font_small.render(item, True, color)
            pos = (self.display.get_width() // 2 - text.get_width() // 2, 250 + i * 50)
            self.menu_item_rects.append(text.get_rect(topleft=pos))
            self.display.blit(text, pos)
        
        audio_on = self.renderer.game_state.audio_manager.sound_enabled
        # Draw music control icon in bottom right corner
        if self.audio_on_icon and self.audio_off_icon:
            icon = self.audio_on_icon if audio_on else self.audio_off_icon
            icon_pos = (self.display.get_width() - 110, self.display.get_height() - 110)
            self.music_icon_rect = icon.get_rect(topleft=icon_pos)
            self.display.blit(icon, icon_pos)
