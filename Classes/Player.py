import pygame as pg
import Classes.Character as chr

from constants import PLAYER_SPEED

class Player(chr.Character):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen):
        pg.draw.rect(screen, (255, 0, 0), (self.position.x, self.position.y, 50, 50))
        
    def update(self):
        self.acc = pg.math.Vector2(0, 0)

        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.move_left()

        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.move_right()

    def move_left(self):
        self.position.x -= PLAYER_SPEED

    def move_right(self):
        self.position.x += PLAYER_SPEED
