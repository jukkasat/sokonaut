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

    def draw_background(self):
        # Draw floor tiles
        for y in range(0, self.display.get_height(), self.tile_size):
            for x in range(0, self.display.get_width(), self.tile_size):
                self.display.blit(self.floor_image, (x, y))

        # Draw walls around the screen using scaled wall tiles
        for x in range(0, self.display.get_width(), self.tile_size):
            self.display.blit(self.wall_image, (x, 0))  # Top wall
            self.display.blit(self.wall_image, (x, self.display.get_height() - self.tile_size))  # Bottom wall
        
        for y in range(0, self.display.get_height(), self.tile_size):  # Adjust vertical range
            self.display.blit(self.wall_image, (0, y))  # Left wall
            self.display.blit(self.wall_image, (self.display.get_width() - self.tile_size, y))  # Right wall
        
        # Draw some decorative boxes and targets
        decorative_elements = [
            (5, 5, 'target'), (5, 6, 'box'),
            (10, 11, 'box'), (10, 12, 'target'),
            (8, 16, 'target'), (9, 16, 'box'),
            (30, 15, 'box'), (31, 15, 'target'),
            (32, 6, 'target'), (32, 7, 'box')
        ]
        for x_tile, y_tile, elem_type in decorative_elements:
            x = x_tile * self.tile_size
            y = y_tile * self.tile_size
            if elem_type == 'box':
                self.display.blit(self.box_image, (x, y))
            else:
                self.display.blit(self.target_image, (x, y))

    def handle_input(self, event):
        pass

    def draw(self):
        pass