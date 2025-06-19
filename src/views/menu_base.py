import os
import pygame
from src.utils.helper import get_base_path

class MenuBase:
    def __init__(self, display, renderer, scores):
        self.display = display
        self.renderer = renderer
        self.scores = scores
        self.menu_font = pygame.font.SysFont("bahnschrift", 100)
        self.menu_font_small = pygame.font.SysFont("bahnschrift", 20)
        self.tile_size = 32
        self.wall_image = pygame.transform.scale(
            renderer.images[1],
            (self.tile_size, self.tile_size)
        )
        self.floor_image = pygame.transform.scale(
            renderer.images[0],
            (self.tile_size, self.tile_size)
        )
        self.box_image = pygame.transform.scale(
            renderer.images[3],
            (self.tile_size, self.tile_size)
        )
        self.target_image = pygame.transform.scale(
            renderer.images[2],
            (self.tile_size, self.tile_size)
        )

    def load_menu_background(self):
        """Load menu background from either development or packaged path"""
        background_path = os.path.join(get_base_path("img"), "menu_background.png")

        try:
            if os.path.exists(background_path):
                background_image = pygame.image.load(background_path)
                return pygame.transform.scale(background_image, 
                    (self.display.get_width(), self.display.get_height())
                )
        except pygame.error as e:
            print(f"Could not load background from {background_path}. Error: {e}")

        return None
        
    def draw_menu_background(self, width, height, x, y):
        menu_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(
            menu_surface,
            (50, 50, 50, 200),  # RGBA: grey with transparency
            (0, 0, width, height),
            border_radius=15
        )
        self.display.blit(menu_surface, (x, y))

