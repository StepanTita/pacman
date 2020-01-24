from model.Objects.Sprites.Sprite import MiddledFieldObject


class Interactable(MiddledFieldObject):
    def __init__(self, images, x, y, width, height, block_width, block_height):
        MiddledFieldObject.__init__(self, images, x, y, width, height, block_width, block_height)


class Coin(Interactable):
    def __init__(self, images, x, y, width, height, block_width, block_height):
        Interactable.__init__(self, images, x, y, width, height, block_width, block_height)


class Point(Interactable):
    def __init__(self, images, x, y, width, height, block_width, block_height):
        Interactable.__init__(self, images, x, y, width, height, block_width, block_height)


class Straw(Interactable):
    def __init__(self, images, x, y, width, height, block_width, block_height):
        super().__init__(images, x, y, width, height, block_width, block_height)


class Rasp(Interactable):
    def __init__(self, images, x, y, width, height, block_width, block_height):
        super().__init__(images, x, y, width, height, block_width, block_height)


class Lemon(Interactable):
    def __init__(self, images, x, y, width, height, block_width, block_height):
        super().__init__(images, x, y, width, height, block_width, block_height)


class Pear(Interactable):
    def __init__(self, images, x, y, width, height, block_width, block_height):
        super().__init__(images, x, y, width, height, block_width, block_height)