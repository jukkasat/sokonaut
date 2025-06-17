import os
import sys
import pygame

class ImageLoader:
    def __init__(self, display):
        self.display = display
        self.tile_sets = self._load_tile_sets()
        self.images = self.tile_sets[0]
        self.level_backgrounds = self._load_level_backgrounds()
        self.game_won_background = self._load_game_won_background()

    def _get_base_path(self):
        """Helper method to determine the correct image directory path"""
        if hasattr(sys, '_MEIPASS'):  # Running as PyInstaller bundle
            return os.path.join(sys._MEIPASS, "src", "img")
        return os.path.join(os.path.dirname(__file__), "..", "img")

    def _load_image(self, path, scale=True):
        """Load an image from the given path and scale it to the display size."""
        try:
            image = pygame.image.load(path)
            if scale:
                image = pygame.transform.scale(image, (self.display.get_width(), self.display.get_height()))
            return image
        except pygame.error as e:
            print(f"Warning: Could not load image {path}. Error: {str(e)}")
            return None

    def _load_tile_sets(self):
        """Load all tile sets into memory."""
        tile_sets = []
        base_path = self._get_base_path()
        
        try:
            for i in range(6):  # 6 tile sets (0-5)
                images = []
                
                # Load each image type
                floor_path = os.path.join(base_path, f"floor{i}.png")
                wall_path = os.path.join(base_path, f"wall{i}.png")
                target_path = os.path.join(base_path, f"target{i}.png")
                barrel_path = os.path.join(base_path, f"barrel{i}.png")
                player_path = os.path.join(base_path, f"player{i}.png")
                ready_path = os.path.join(base_path, f"ready{i}.png")
                robotarget_path = os.path.join(base_path, f"robotarget{i}.png")

                images.append(pygame.image.load(floor_path))
                images.append(pygame.image.load(wall_path))
                images.append(pygame.image.load(target_path))
                images.append(pygame.image.load(barrel_path))
                images.append(pygame.image.load(player_path))
                images.append(pygame.image.load(ready_path))
                images.append(pygame.image.load(robotarget_path))

                tile_sets.append(images)
        except Exception as e:
            print(f"Error loading images: {str(e)}")
            return []
            
        return tile_sets

    def _load_level_backgrounds(self):
        """Load all level background images."""
        level_backgrounds = []
        base_path = self._get_base_path()
        
        try:
            for i in range(0, 6):  # 6 set of level backgrounds 
                image_path = os.path.join(base_path, f"level_background{i}.png")
                level_backgrounds.append(self._load_image(image_path))
            return level_backgrounds
        except Exception as e:
            print(f"Error loading level backgrounds: {str(e)}")
            return []

    def _load_game_won_background(self):
        """Load the game won background image."""
        base_path = self._get_base_path()
        
        try:
            image_path = os.path.join(base_path, "game_won_background.png")
            return self._load_image(image_path)
        except Exception as e:
            print(f"Error loading game won background: {str(e)}")
            return None