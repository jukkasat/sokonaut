import pygame
from src.utils.image_loader import ImageLoader
from src.utils.ui_drawer import UIDrawer
from src.views.game_won_view import GameWonView
from src.views.level_won_view import LevelWonView

class Renderer:
    def __init__(self, game_state, display, scores):
        self.game_state = game_state
        self.display = display
        self.image_loader = ImageLoader(display)
        self.images = self.image_loader.images
        self.font = pygame.font.SysFont("bahnschrift", 24)
        self.ui_drawer = UIDrawer(display, game_state, self.font)
        self.game_won_view = GameWonView(display, game_state, self.font, self.image_loader, self.ui_drawer)
        self.level_won_view = LevelWonView(display, game_state, self.font, scores, self.ui_drawer)
        
        # Calculate scaling based on the first tile
        base_width = self.images[0].get_width()
        self.scale_factor = self.display.get_width() / (self.game_state.width * base_width)
        self.tile_size = int(self.image_loader.images[0].get_width() * self.scale_factor)
        self.offset_x = 0
        self.offset_y = (self.display.get_height() - (self.game_state.height * self.tile_size)) // 2

        # Initialize scaled images and cache them
        self.scaled_images = self._scale_images()
        self.menu_bg_width = self.display.get_width() // self.tile_size
        self.menu_bg_height = self.display.get_height() // self.tile_size

        # Store the previous map dimensions to detect changes
        self.prev_map_width = self.game_state.width
        self.prev_map_height = self.game_state.height

    def _scale_images(self):
        """Scale all images and return them in a list"""
        scaled_images = []
        for image in self.image_loader.images:
            scaled = pygame.transform.scale(image, (self.tile_size, self.tile_size))
            scaled_images.append(scaled)
        return scaled_images

    def draw(self):
        # Update scaling if map dimensions have changed
        if (self.game_state.width != self.prev_map_width or
            self.game_state.height != self.prev_map_height):
            self.update_scaling()

        self.display.fill((0, 0, 0))

        # Determine which images to use based on the level
        background_index = None
        tile_set_index = None

        if self.game_state.current_level == 0:
            background_index = 0
            tile_set_index = 0
        elif 1 <= self.game_state.current_level <= 5:
            background_index = 1
            tile_set_index = 1
        elif 6 <= self.game_state.current_level <= 10:
            background_index = 2
            tile_set_index = 2
        elif 11 <= self.game_state.current_level <= 15:
            background_index = 3
            tile_set_index = 3
        elif 16 <= self.game_state.current_level <= 20:
            background_index = 4
            tile_set_index = 4
        elif self.game_state.current_level == 21:
            background_index = 5
            tile_set_index = 5

        # Draw level background image
        if (background_index is not None and
            background_index < len(self.image_loader.level_backgrounds) and
            self.image_loader.level_backgrounds[background_index]):
            self.display.blit(self.image_loader.level_backgrounds[background_index], (0, 0))

        # Set the current tile set
        if tile_set_index is not None and tile_set_index < len(self.image_loader.tile_sets):
            self.image_loader.images = self.image_loader.tile_sets[tile_set_index]
            self.update_scaling()  # Update scaling with the new images

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

        self.ui_drawer.draw_ui()

        # Check if all levels are completed
        if self.game_state.game_completed():
            self.game_won_view.draw()
        # Check if level is completed
        elif self.game_state.level_won():
            self.level_won_view.draw()

    def update_scaling(self):
        """Update scaling factors when map dimensions change"""
        # Get current map dimensions
        map_width = len(self.game_state.map[0])
        map_height = len(self.game_state.map)

        # Calculate scaling to fit screen width and height
        width_scale = self.display.get_width() / (map_width * self.image_loader.images[0].get_width())
        height_scale = (self.display.get_height() * 0.8) / (map_height * self.image_loader.images[0].get_height())

        # Use the smaller scale to ensure the map fits both dimensions
        self.scale_factor = min(width_scale, height_scale)
        self.tile_size = int(self.image_loader.images[0].get_width() * self.scale_factor)

        # Calculate centering offsets
        self.offset_x = (self.display.get_width() - (map_width * self.tile_size)) // 2
        self.offset_y = (self.display.get_height() - (map_height * self.tile_size)) // 2

        # Update scaled images
        self.scaled_images = self._scale_images()

        # Store the current map dimensions
        self.prev_map_width = map_width
        self.prev_map_height = map_height