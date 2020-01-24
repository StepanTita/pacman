from model.Objects.Sprites.Sprite import FieldObject, MiddledFieldObject


class Interactable(MiddledFieldObject):
    def __init__(self, images, x, y, width, height, block_width, block_height):
        MiddledFieldObject.__init__(self, images, x, y, width, height, block_width, block_height)


class Coin(Interactable):
    def __init__(self, images, x, y, width, height, block_width, block_height):
        Interactable.__init__(self, images, x, y, width, height, block_width, block_height)


class Point(Interactable):
    def __init__(self, images, x, y, width, height, block_width, block_height):
        Interactable.__init__(self, images, x, y, width, height, block_width, block_height)