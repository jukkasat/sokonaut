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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move(0, -1)
                if event.key == pygame.K_RIGHT:
                    self.move(0, 1)
                if event.key == pygame.K_UP:
                    self.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    self.move(1, 0)

            if event.type == pygame.QUIT:
                exit()

    def draw_display(self):
        self.display.fill((0, 0, 0))

        for y in range(self.height):
            for x in range(self.width):
                tile = self.map[y][x]
                self.display.blit(self.images[tile], (x * self.scale, y * self.scale))

        pygame.display.flip()

    def find_robo(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in [4, 6]:
                    return (y, x)
                
    def move(self, move_y, move_x):
        robon_vanha_y, robon_vanha_x = self.find_robo()
        robon_uusi_y = robon_vanha_y + move_y
        robon_uusi_x = robon_vanha_x + move_x

        if self.map[robon_uusi_y][robon_uusi_x] == 1:
            return

        if self.map[robon_uusi_y][robon_uusi_x] in [3, 5]:
            laatikon_uusi_y = robon_uusi_y + move_y
            laatikon_uusi_x = robon_uusi_x + move_x

            if self.map[laatikon_uusi_y][laatikon_uusi_x] in [1, 3, 5]:
                return

            self.map[robon_uusi_y][robon_uusi_x] -= 3
            self.map[laatikon_uusi_y][laatikon_uusi_x] += 3

        self.map[robon_vanha_y][robon_vanha_x] -= 4
        self.map[robon_uusi_y][robon_uusi_x] += 4