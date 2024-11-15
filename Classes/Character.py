import pygame as pg
import Classes.Entity as ent

class Character(ent.Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.velocity = pg.math.Vector2(0, 0)
        self.acceleration = pg.math.Vector2(0, 0)
    
    def is_on_surface(self, surface_group):
        hits = pg.sprite.spritecollide(self, surface_group, False)

        if hits:
            top = hits[0].rect.top

            self.position.y = top - 49
            self.velocity.y = 0
