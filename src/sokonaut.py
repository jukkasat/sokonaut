import pygame

class Sokonaut:
    def __init__(self):
        pygame.init()
        
        self.load_images()
        self.new_game()
        
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.scale = self.images[0].get_width()

        display_height = self.scale * self.height
        display_width = self.scale * self.width
        self.display = pygame.display.set_mode((display_width, display_height))

        pygame.display.set_caption("Sokonaut 1")

        self.loop()

    def load_images(self):
        self.images = []
        for name in ["lattia", "seina", "kohde", "laatikko", "robo", "valmis", "kohderobo"]:
            self.images.append(pygame.image.load("src/img/" + name + ".png"))

    def new_game(self):
        self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                [1, 2, 3, 0, 0, 0, 1, 0, 0, 1, 2, 3, 0, 0, 0, 0, 1],
                [1, 0, 0, 1, 2, 3, 0, 2, 3, 0, 0, 0, 1, 0, 0, 0, 1],
                [1, 0, 4, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def loop(self):
        while True:
            self.check_events()
            self.draw_display()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def draw_display(self):
        self.display.fill((0, 0, 0))

        for y in range(self.height):
            for x in range(self.width):
                tile = self.map[y][x]
                self.display.blit(self.images[tile], (x * self.scale, y * self.scale))

        pygame.display.flip()