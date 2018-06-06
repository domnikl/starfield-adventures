import sys
import pygame
import random
import spritesheet
from spaceship import Spaceship
from enemy import Enemies
import stars
import os

class Game(object):
    def __init__(self):
        self.score = 0

    def killed_enemy(self, enemy):
        self.score += enemy.speed * 100

    def got_killed(self):
        self.score = int(self.score / 2)

def main():
    game = Game()

    pygame.init()
    clock = pygame.time.Clock()
    myfont = pygame.font.Font(None, 30)

    info = pygame.display.Info()
    width = int(info.current_w / 2)
    height = int(info.current_h / 2)

    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE|pygame.DOUBLEBUF)

    starfield = stars.Starfield(width, height)

    spaceship = Spaceship(width, height, spritesheet.spritesheet(os.path.dirname(os.path.realpath(__file__)) + "/spaceship.png"))
    
    ss = spritesheet.spritesheet(os.path.dirname(os.path.realpath(__file__)) + "/enemy1.png")

    enemy_sprites = [ss.images_at(
            [(0, 0, 32, 32), 
            (0, 32, 32, 32),
            (0, 64, 32, 32),
            (0, 96, 32, 32)],
            colorkey=(0, 0, 0)
        )]

    enemies = Enemies(width, height, enemy_sprites)

    game_objects = [
        starfield,
        spaceship,
        enemies
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_LEFT:
                    spaceship.move("left")
                elif event.key == pygame.K_RIGHT:
                    spaceship.move("right")
                elif event.key == pygame.K_SPACE:
                    spaceship.shoot()
 
        for movable in game_objects:
            movable.update()

        for e in spaceship.shot_enemies(enemies):
            game.killed_enemy(e)
            enemies.kill(e)

        for e in spaceship.colliding_enemies(enemies):
            game.got_killed()
            enemies.kill(e)

        screen.fill((0, 0, 0))

        for drawable in game_objects:
            drawable.draw(screen)

        label = myfont.render(str(game.score), 1, (255,255,0))
        screen.blit(label, (20, 20))

        pygame.display.flip()
        clock.tick(120) # FPS

if __name__ == '__main__':
    random.seed()
    main()
