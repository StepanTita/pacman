from itertools import cycle

from model.Objects.Sprites.Sprite import FieldObject
from model.utils.Utils import ImageUtils


class Wall(FieldObject):

    def __init__(self, images, x, y, width, height, block_width, block_height):
        FieldObject.__init__(self, images, x, y, width, height, block_width, block_height)

        self._states = cycle(self._images)
        self._current_state = None

        self.next_state()
