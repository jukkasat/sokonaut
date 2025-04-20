import pygame

class ImageLoader:
    def __init__(self, display):
        self.display = display
        self.images = self._load_images()
        self.level_backgrounds = self._load_level_backgrounds()
        self.game_won_background = self._load_game_won_background()

    def _load_images(self):
        # Load images for the game tiles
        images = []
        for name in ["floor1", "wall1", "target1", "barrel1", "player3", "ready1", "robotarget1"]:
            try:
                image = pygame.image.load("src/img/" + name + ".png")
                images.append(image)
            except pygame.error as e:
                print(f"Warning: Could not load image '{name}'. Error: {e}")
                images.append(None)  # Append None to maintain index consistency

        if not images:
            raise RuntimeError("No images were loaded. Ensure the image files exist in 'src/img/'.")

        return images

    def _load_level_backgrounds(self):
        level_backgrounds = []
        for i in range(0, 6):  # Load level_background0.png to level_background6.png
            try:
                background_image = pygame.image.load(f"src/img/level_background{i}.png")
                level_backgrounds.append(pygame.transform.scale(background_image, (self.display.get_width(), self.display.get_height())))
            except pygame.error as e:
                print(f"Warning: Could not load level background image {i}. Error: {e}")
                level_backgrounds.append(None)
        return level_backgrounds

    def _load_game_won_background(self):
        try:
            background_image = pygame.image.load("src/img/game_won_background.png")
            return pygame.transform.scale(background_image, (self.display.get_width(), self.display.get_height()))
        except pygame.error as e:
            print(f"Warning: Could not load level won background image. Error: {e}")
            return None