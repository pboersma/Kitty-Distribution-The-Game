import pygame as pg

from constants import DISPLAY_WIDTH, DISPLAY_HEIGHT

import Classes.Entity as ent

class Platform(ent.Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen):
        pg.draw.line(screen, (0, 255, 0), (0, DISPLAY_HEIGHT), (DISPLAY_WIDTH, DISPLAY_HEIGHT), 10)

