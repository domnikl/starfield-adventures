import pygame

class Shot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
    
    def update(self):
        self.y -= self.speed

    def draw(self, surface):
        pygame.draw.line(surface, (220, 20, 60), [self.x, self.y], [self.x, self.y + 10])

    def is_in_bounding_box(self, lx, ly, rx, ry):
        #right = self.x >= lx and self.y >= ly and self.x <= rx and self.y <= ry
        #left = self.x + self.width >= lx and self.y + self.height >= ly


        return self.x >= lx and self.y >= ly and self.x <= rx and self.y <= ry
