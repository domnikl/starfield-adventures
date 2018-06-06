import sys
import pygame
import random

pygame.init()

info = pygame.display.Info()
width = info.current_w / 2
height = info.current_h / 2

size = width, height
speed = [10, 0]
black = 0, 0, 0
white = (255, 255, 255)

random.seed()

screen = pygame.display.set_mode(size)

class Star:
    def __init__(self, init_x, init_y, size, speed, color):
        self.position = [init_x, init_y]
        self.size = size
        self.speed = speed
        self.color = color
    
    def move(self):
        self.position[1] += self.speed

    def is_in_field(self, width, height):
        x = self.position[0]
        y = self.position[1]

        return x > 0 and x < width and y > 0 and y < height

    def render(self, surface):
        start_pos = self.position
        end_pos = [self.position[0], self.position[1] + self.size]

        pygame.draw.line(surface, self.color, start_pos, end_pos)

class Starfield:
    def __init__(self, width, height):
        self.stars = []
        self.width = width
        self.height = height

        for _i in range(0, 100):
            self._add_new_random_star(random.randint(0, self. height - 1))

    def _add_new_random_star(self, init_y):
        init_x = random.randint(0, self.width - 1)
        distance = random.randint(1, 10)

        size = distance
        speed = distance
        color = (255 - distance * 5, 255 - distance * 5, 255 - distance * 5)

        self.stars.append(Star(init_x, init_y, size, speed, color))

    def move(self):
        remaining_stars = []
        for star in self.stars:
            star.move()

            if star.is_in_field(self.width, self.height):
                remaining_stars.append(star)
            else:
                self._add_new_random_star(0)
            
        self.stars = remaining_stars

    def render(self, surface):
        for star in self.stars:
            star.render(surface)

starfield = Starfield(width, height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    starfield.move()
    
    screen.fill(black)
    starfield.render(screen)
    pygame.display.flip()
