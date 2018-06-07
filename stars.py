import random
import pygame
import math
import numpy

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
        self.star_count = 75

        for _i in range(0, self.star_count):
            self._add_new_random_star(self._new_y_for_new_star())

    def _add_new_random_star(self, init_y):
        init_x = self._new_x_for_new_star()

        distance = abs(int(numpy.random.normal(0, 7, 1)[0]))
        #distance = int(math.log10(random.randint(1, 12)) * 10)

        size = distance
        speed = distance
        color = 100 + distance * 20

        # color should not depend on distance!

        if color > 255:
            color = 255

        color = (color, color, color)

        self.stars.append(Star(init_x, init_y, size, speed, color))

    def _new_y_for_new_star(self):
        return abs(int(numpy.random.normal(0, self.height, 1)[0]))

    def _new_x_for_new_star(self):
        half = int(self.width / 2)

        if len(self.stars) == 0:
            return half

        last = self.stars[len(self.stars) - 1]

        if last.position[0] > half:
            x = abs(int(numpy.random.normal(0, last.position[0], 1)[0]))
        else:
            x = abs(int(numpy.random.normal(last.position[0], self.width, 1)[0]))

        if abs(last.position[0] - x) < 50:
            return self._new_x_for_new_star()

        return x
    
    def update(self):
        self.stars = [x for x in self.stars if x.is_in_field(self.width, self.height)]

        missing_stars = self.star_count - len(self.stars)
        missing_stars += random.randint(0, 10)

        for _i in range(0, missing_stars):
            self._add_new_random_star(0)

        for star in self.stars:
            star.move()

    def draw(self, surface):
        for star in self.stars:
            star.draw(surface)
