import pygame as pg

class Entity(pg.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pg.math.Vector2(x, y)

    def update(self, delta):
        pass

    def draw(self, screen):
        pass
