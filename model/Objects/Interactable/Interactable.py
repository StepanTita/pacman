from itertools import cycle

from model.Objects.Sprites.Sprite import FieldObject


class Coin(FieldObject):
    def __init__(self, images, x, y, width, height):
        FieldObject.__init__(self, x, y, width, height)

        self._images = images
        self._states = cycle(self._images)
        self._current_state = None

        self.next_state()