import random

class Enemies(object):
    def __init__(self, width, height, sprite_sets):
        self.sprites = sprite_sets[0]

        self.width = width
        self.height = height
        self.enemies = []
        self._add_random_enemy()

    def _add_random_enemy(self):
        speed = random.randint(1, 3)
        init_x = random.randint(0, self.width)

        self.enemies.append(Enemy(init_x, speed, self.sprites))

    def update(self):
        enemies = []
        for enemy in self.enemies:
            enemy.update()

            if enemy.is_in_rect(0, 0, self.width, self.height):
                enemies.append(enemy)
            else:
                self._add_random_enemy()

            if random.randint(0, 1000) > 999:
                self._add_random_enemy()

        self.enemies = enemies
        
    def draw(self, surface):
        for enemy in self.enemies:
            enemy.draw(surface)

    def is_enemy_in_bounding_box(self, lx, ly, rx, ry):
        for enemy in self.enemies:
            if enemy.is_in_rect(lx, ly, rx, ry):
                return True
        
        return False

class Enemy(object):
    def __init__(self, init_x, speed, sprites):
        self.x = init_x
        self.y = 0
        self.speed = speed
        self.image_index = 0
        self.images = sprites

    def update(self):
        self.y += self.speed

    def draw(self, surface):
        self.image_index += 1

        if self.image_index >= len(self.images):
            self.image_index = 0

        surface.blit(self.images[self.image_index], (self.x, self.y))

    def is_in_rect(self, lx, ly, rx, ry):
        return self.x >= lx and self.y >= ly and self.x <= rx and self.y <= ry
    