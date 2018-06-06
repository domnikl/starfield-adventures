import random
import pygame

class Star(object):
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

    def draw(self, surface):
        start_pos = self.position
        end_pos = [self.position[0], self.position[1] + self.size]

        pygame.draw.line(surface, self.color, start_pos, end_pos)


class Starfield(object):
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
        color = (255 - distance * 10, 255 - distance * 10, 255 - distance * 10)

        self.stars.append(Star(init_x, init_y, size, speed, color))

    def update(self):
        remaining_stars = []
        for star in self.stars:
            star.move()

            if star.is_in_field(self.width, self.height):
                remaining_stars.append(star)
            else:
                self._add_new_random_star(0)
            
        self.stars = remaining_stars

    def draw(self, surface):
        for star in self.stars:
            star.draw(surface)
