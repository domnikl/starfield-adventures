import random

class Spaceship(object):
    def __init__(self, surface_x, surface_y, spritesheet):
        self.width = 32
        self.height = 32
        self.x = surface_x / 2
        self.y = surface_y - 50
        self.surface_x = surface_x
        self.surface_y = surface_y
        self.speed = 0
        self.direction = 0
        self.image_index = 0
        self.images = spritesheet.images_at(
            [(0, 0, 32, 32), 
            (0, 32, 32, 32),
            (0, 64, 32, 32),
            (32, 0, 32, 32),
            (32, 32, 32, 32)],
            colorkey=(0, 0, 0)
        )

    def move(self, direction):
        if self.speed <= 0:
            self.direction = direction
            self.speed = random.randint(1, 2)
        if self.direction != direction:
            self.speed -= 3 # slow down faster
        else:
            self.speed += 3

        if self.speed > 20:
            self.speed = 20
        
    def update(self):
        if self.direction == "left":
            self.x -= self.speed
        elif self.direction == "right":
            self.x += self.speed

        if self.x > self.surface_x:
            self.x = 0
        
        if self.x + self.width < 0:
            self.x = self.surface_x
        
    def draw(self, surface):
        self.image_index += 1

        if self.image_index >= len(self.images):
            self.image_index = 0

        surface.blit(self.images[self.image_index], (self.x, self.y))

    def is_colliding_with(self, enemies):
        return enemies.is_enemy_in_bounding_box(self.x, self.y, self.x + self.width, self.y + self.height)
