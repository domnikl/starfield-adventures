import random

class Enemies(object):
    def __init__(self, surface_width, surface_height, sprite_sets):
        self.sprites = sprite_sets[0]

        self.surface_width = surface_width
        self.surface_height = surface_height
        self.width = 32
        self.additional_enemy_propability = 999
        self.enemies = {}
        self._add_random_enemy()

    def _add_random_enemy(self):
        speed = random.randint(1, 3)
        init_x = random.randint(0, self.surface_width - self.width)

        self.enemies[init_x] = Enemy(init_x, speed, self.sprites)

    def update(self):
        for _, enemy in self.enemies.copy().items():
            enemy.update()

            if not enemy.is_in_rect(0, 0, self.surface_width, self.surface_height):
                self._remove(enemy)

    def kill(self, enemy):
        self.additional_enemy_propability -= 3
        self._remove(enemy)

    def _remove(self, enemy):
        del self.enemies[enemy.x]
        self._add_random_enemy()

        if random.randint(0, 1000) > self.additional_enemy_propability:
            self._add_random_enemy()

    def draw(self, surface):
        for _, enemy in self.enemies.items():
            enemy.draw(surface)

    def enemies_in_bounding_box(self, lx, ly, rx, ry):
        enemies = []

        for _, enemy in self.enemies.items():
            if enemy.is_in_rect(lx, ly, rx, ry):
                enemies.append(enemy)
        
        return enemies

class Enemy(object):
    def __init__(self, init_x, speed, sprites):
        self.x = init_x
        self.y = 0
        self.width = 32
        self.height = 32
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
        my_rx = self.x + self.width
        my_ry = self.y + self.height

        left = self.x >= lx and self.y >= ly and self.x <= rx and self.y <= ry
        right = my_rx >= lx and my_ry >= ly and my_rx <= rx and my_ry <= ry

        return left or right
