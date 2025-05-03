import pygame

class ImageLoader:
    def __init__(self, display):
        self.display = display
        self.tile_sets = self._load_tile_sets()
        self.images = self.tile_sets[0]
        self.level_backgrounds = self._load_level_backgrounds()
        self.game_won_background = self._load_game_won_background()

    def _load_image(self, path, scale=True):
        """Load an image from the given path and scale it to the display size."""
        try:
            image = pygame.image.load(path)
            if scale:
                image = pygame.transform.scale(image, (self.display.get_width(), self.display.get_height()))
            return image
        except pygame.error as e:
            print(f"Warning: Could not load image {path}. Error: {e}")
            return None

    def _load_level_backgrounds(self):
        level_backgrounds = []
        for i in range(0, 6):  # Load level_background0.png to level_background6.png
            level_backgrounds.append(self._load_image(f"src/img/level_background{i}.png"))
        return level_backgrounds
    
    def _load_tile_sets(self):
        tile_sets = []
        for i in range(6):  # Load floor0.png/wall0.png to floor5.png/wall5.png
            images = []
            try:
                floor_image = pygame.image.load(f"src/img/floor{i}.png")
                images.append(floor_image)
                wall_image = pygame.image.load(f"src/img/wall{i}.png")
                images.append(wall_image)
                target_image = pygame.image.load(f"src/img/target{i}.png")
                images.append(target_image)
                barrel_image = pygame.image.load(f"src/img/barrel{i}.png")
                images.append(barrel_image)
                player_image = pygame.image.load(f"src/img/player{i}.png")
                images.append(player_image)
                ready_image = pygame.image.load(f"src/img/ready{i}.png")
                images.append(ready_image)
                robotarget_image = pygame.image.load(f"src/img/robotarget{i}.png")
                images.append(robotarget_image)
            except pygame.error as e:
                print(f"Warning: Could not load tile set {i}. Error: {e}")
                # Append None for each image in the set to maintain index consistency
                images = [None] * 7
            tile_sets.append(images)

        if not tile_sets:
            raise RuntimeError("No tile sets were loaded. Ensure the image files exist in 'src/img/'.")

        return tile_sets

    def _load_game_won_background(self):
        return self._load_image("src/img/game_won_background.png")