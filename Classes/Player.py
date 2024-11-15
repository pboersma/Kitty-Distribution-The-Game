import pygame as pg
import Classes.Character as chr

from constants import DISPLAY_WIDTH, PLAYER_ACCELERATION, PLAYER_FRICTION

class Player(chr.Character):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen):
        self.rect = pg.draw.rect(screen, (255, 0, 0), (self.position.x, self.position.y, 50, 50))

    def update(self, delta):
        self.acceleration = pg.math.Vector2(0, 0.5)

        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.move_left()

        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.move_right()

        if keys[pg.K_SPACE]:
            self.jump()

        self.acceleration.x += self.velocity.x * PLAYER_FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration
     
    def move_left(self):
        self.acceleration.x = -PLAYER_ACCELERATION

    def move_right(self):
        self.acceleration.x = PLAYER_ACCELERATION

    def jump(self):
        self.velocity.y = -15
