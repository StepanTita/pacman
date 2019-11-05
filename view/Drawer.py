from .Color import Color


class Drawer:

    def __init__(self, screen, pg):
        self.screen = screen
        self.pg_obj = pg
        ...  # TODO


class SpriteDrawer:

    def __init__(self, sprite):
        super().__init__()
        self.sprite = sprite

    def draw(self):
        self.pg_obj.draw.rect(self.screen, Color.WHITE, (self.sprite.x, self.sprite.y, self.sprite.width, self.sprite.height))
