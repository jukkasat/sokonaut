import pygame

class MenuBase:
    def __init__(self, display, renderer, high_scores=None):
        self.display = display
        self.renderer = renderer
        self.high_scores = high_scores
        self.menu_font = pygame.font.SysFont("Arial", 74)
        self.menu_font_small = pygame.font.SysFont("Arial", 20)
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
        try:
            background_image = pygame.image.load("src/img/background1.png")
            return pygame.transform.scale(background_image, (self.display.get_width(), self.display.get_height()))
        except pygame.error as e:
            print(f"Warning: Could not load background image. Error: {e}")
            return None

    def handle_input(self, event):
        pass

    def draw(self):
        pass