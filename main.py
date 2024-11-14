import pygame as pg
import sys

from constants import DISPLAY_WIDTH, DISPLAY_HEIGHT

import Classes.Player as plr
import Classes.Platform as plt

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.clock = pg.time.Clock()

    def run(self):
        self._register_entities()

        while True:
            self._register_events()

            self.screen.fill((0,0,0))

            self._register_logic()

            self._update()

            delta = self.clock.tick(60)

    def _register_events(self):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

    def _update(self):
        pg.display.update()

    def _register_entities(self):
        self.drawable = pg.sprite.Group()
        self.updateable = pg.sprite.Group()

        plr.Player.containers = (self.drawable, self.updateable)
        self.player = plr.Player(DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2)

        plt.Platform.containers = (self.drawable, )
        self.platform = plt.Platform(DISPLAY_HEIGHT, DISPLAY_WIDTH)
        
    def _register_logic(self):
        for entity in self.drawable:
            entity.draw(self.screen)

        for entity in self.updateable:
            entity.update()

if __name__ == "__main__":
    pg.init()
    game = Game()
    game.run()
