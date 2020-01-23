from itertools import cycle

from pygame.sprite import Group

from model.Dependencies.Dependencies import Dependencies
from model.Objects.Interactable.Interactable import Coin
from model.Objects.Sprites.Sprite import Pacman, SlowGhost, FastGhost, SleepingGhost, MutantGhost
from model.Objects.background.Wall import Wall
from model.utils.Utils import ImageUtils, BaseUtils


class MultipleObjectsGenerator:

    def __init__(self):
        self._container = Group()

    def _add(self, field_object):
        self._container.add(field_object)

    def get_field_objects(self):
        return self._container


class SingleObjectGenerator:

    def __init__(self):
        self._field_object = None

    def _add(self, field_object):
        self._field_object = field_object

    def get_field_object(self):
        return self._field_object


class ObjectGenerator:
    def __init__(self, block_width, block_height,
                 field_object_width, field_object_height, field_object_types):
        self._block_width = block_width
        self._block_height = block_height
        self._field_object_width = field_object_width
        self._field_object_height = field_object_height
        self._field_object_types = field_object_types
        self._field_object_type = self._field_object_types[0]

    def _read_images(self, img, img_pos):
        return ImageUtils.crop_image(
            base_img=Dependencies.load_img(img),
            img_pos=img_pos
        )

    def init_images(self, img, img_pos, split_by=0):
        images = self._read_images(img, img_pos)
        self._split_images(images, split_by)

    def _split_images(self, images, split_by=0):
        if split_by == 0:
            self._images = [images]
        else:
            self._images = BaseUtils.divide_chunks(images, split_by)

    def set_type(self, type_id):
        self._current_type = self._images[type_id]
        self._field_object_type = self._field_object_types[type_id]

    def generate(self, field):
        for i in range(field.rows_count):
            for j in range(field.cols_count):
                if type(field[i][j]) in self._field_object_types:
                    self._add(field[i][j])


class MoveableObjectCreator(ObjectGenerator):

    def __init__(self, horizontal_speed, vertical_speed, block_width, block_height,
                 field_object_width, field_object_height, field_object_types):
        super().__init__(block_width, block_height, field_object_width, field_object_height, field_object_types)
        self._horizontal_speed = horizontal_speed
        self._vertical_speed = vertical_speed

    def create(self, row, col):
        return self._field_object_type(images=self._current_type,
                                       horizontal_speed=self._horizontal_speed, vertical_speed=self._vertical_speed,
                                       x=col * self._block_width, y=row * self._block_height,
                                       width=self._field_object_width, height=self._field_object_height,
                                       block_width=self._block_width, block_height=self._block_height)


class StaticObjectCreator(ObjectGenerator):

    def __init__(self, block_width, block_height,
                 field_object_width, field_object_height, field_object_types):
        super().__init__(block_width, block_height, field_object_width, field_object_height, field_object_types)

    def create(self, row, col):
        return self._field_object_type(images=self._current_type,
                                       x=col * self._block_width, y=row * self._block_height,
                                       width=self._field_object_width, height=self._field_object_height,
                                       block_width=self._block_width, block_height=self._block_height)


class PacmanGenerator(MoveableObjectCreator, SingleObjectGenerator):
    def __init__(self, block_width, block_height,
                 field_object_width, field_object_height,
                 horizontal_speed, vertical_speed):
        MoveableObjectCreator.__init__(self, horizontal_speed=horizontal_speed, vertical_speed=vertical_speed,
                                       block_width=block_width, block_height=block_height,
                                       field_object_width=field_object_width, field_object_height=field_object_height,
                                       field_object_types=(Pacman,))
        SingleObjectGenerator.__init__(self)


class WallGenerator(StaticObjectCreator, MultipleObjectsGenerator):
    """
    Builder Pattern
    """

    def __init__(self, block_width, block_height, field_object_width, field_object_height):
        StaticObjectCreator.__init__(self, block_width, block_height, field_object_width, field_object_height, (Wall,))
        MultipleObjectsGenerator.__init__(self)


class CoinGenerator(StaticObjectCreator, MultipleObjectsGenerator):

    def __init__(self, block_width, block_height, field_object_width, field_object_height):
        StaticObjectCreator.__init__(self, block_width, block_height, field_object_width, field_object_height, (Coin,))
        MultipleObjectsGenerator.__init__(self)


class GhostGenerator(MoveableObjectCreator, MultipleObjectsGenerator):

    def __init__(self, block_width, block_height,
                 field_object_width, field_object_height,
                 horizontal_speed, vertical_speed):
        MoveableObjectCreator.__init__(self, horizontal_speed=horizontal_speed, vertical_speed=vertical_speed,
                                       block_width=block_width, block_height=block_height,
                                       field_object_width=field_object_width,
                                       field_object_height=field_object_height,
                                       field_object_types=(MutantGhost, SlowGhost, FastGhost, SleepingGhost))
        MultipleObjectsGenerator.__init__(self)
