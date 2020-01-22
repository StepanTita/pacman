from itertools import cycle

from model.Objects.Sprites.Sprite import FieldObject
from model.utils.Utils import ImageUtils


class Coin(FieldObject):
    def __init__(self, images, x, y, width, height):
        FieldObject.__init__(self, images, x, y, width, height)

        self._states = cycle(self._images)
        self._current_state = None

        self.next_state()