from consts import *


class Sprite:
    def __init__(self, x=DEFAULT_X, y=DEFAULT_Y, width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.image = ...  # TODO

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


class Pacman(Sprite):
    def __init__(self):
        super().__init__()


class Ghost(Sprite):
    def __init__(self):
        super().__init__()
