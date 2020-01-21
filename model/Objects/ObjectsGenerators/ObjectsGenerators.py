from pygame.sprite import Group

from model.Dependencies.Dependencies import Dependencies
from model.Objects.Interactable.Interactable import Coin
from model.Objects.Sprites.Sprite import Ghost, Pacman
from model.Objects.background.Wall import Wall
from model.utils.ImageUtils import ImageUtils


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
                 field_object_width, field_object_height, field_object_type):
        self._block_width = block_width
        self._block_height = block_height
        self._field_object_width = field_object_width
        self._field_object_height = field_object_height
        self._field_object_type = field_object_type

    def init_images(self, img, img_pos):
        self._images = ImageUtils.resize_images(
            ImageUtils.crop_image(
                base_img=Dependencies.load_img(img),
                img_pos=img_pos
            ), target_width=self._field_object_width, target_height=self._field_object_height
        )

    def generate(self, field):
        for i in range(field.rows_count):
            for j in range(field.cols_count):
                if type(field[i][j]) is self._field_object_type:
                    self._add(field[i][j])


class MoveableObjectCreator(ObjectGenerator):

    def __init__(self, horizontal_speed, vertical_speed, block_width, block_height,
                 field_object_width, field_object_height, field_object_type):
        super().__init__(block_width, block_height, field_object_width, field_object_height, field_object_type)
        self._horizontal_speed = horizontal_speed
        self._vertical_speed = vertical_speed

    def create(self, row, col):
        return self._field_object_type(images=self._images,
                                       horizontal_speed=self._horizontal_speed, vertical_speed=self._vertical_speed,
                                       x=col * self._block_width, y=row * self._block_height,
                                       width=self._field_object_width, height=self._field_object_height)


class StaticObjectCreator(ObjectGenerator):

    def __init__(self, block_width, block_height,
                 field_object_width, field_object_height, field_object_type):
        super().__init__(block_width, block_height, field_object_width, field_object_height, field_object_type)

    def create(self, row, col):
        return self._field_object_type(images=self._images,
                                       x=col * self._block_width, y=row * self._block_height,
                                       width=self._field_object_width, height=self._field_object_height)


class PacmanGenerator(MoveableObjectCreator, SingleObjectGenerator):
    def __init__(self, block_width, block_height,
                 field_object_width, field_object_height,
                 horizontal_speed, vertical_speed):
        MoveableObjectCreator.__init__(self, horizontal_speed=horizontal_speed, vertical_speed=vertical_speed,
                                       block_width=block_width, block_height=block_height,
                                       field_object_width=field_object_width, field_object_height=field_object_height,
                                       field_object_type=Pacman)
        SingleObjectGenerator.__init__(self)


class WallGenerator(StaticObjectCreator, MultipleObjectsGenerator):
    """
    Builder Pattern
    """

    def __init__(self, block_width, block_height, field_object_width, field_object_height):
        StaticObjectCreator.__init__(self, block_width, block_height, field_object_width, field_object_height, Wall)
        MultipleObjectsGenerator.__init__(self)

    # def generate_walls(self, x1, y1, x2, y2, block_width, block_height):
    #     for i in range(x1, x2):
    #         for j in range(y1, y2):
    #             self._walls.add(Wall(images=self._images, x=i * block_width, y=j * block_height,
    #                                  width=block_width, height=block_height))

    # def generate_frame(self, rows_count, cols_count, block_width, block_height):
    #     self.generate_walls(x1=0, x2=cols_count,
    #                         y1=0, y2=1,
    #                         block_width=block_width, block_height=block_height)
    #     self.generate_walls(x1=0, x2=cols_count,
    #                         y1=rows_count - 1, y2=rows_count,
    #                         block_width=block_width, block_height=block_height)
    #     self.generate_walls(x1=0, x2=1,
    #                         y1=0, y2=rows_count,
    #                         block_width=block_width, block_height=block_height)
    #     self.generate_walls(x1=cols_count - 1, x2=cols_count,
    #                         y1=0, y2=rows_count,
    #                         block_width=block_width, block_height=block_height)


class CoinGenerator(StaticObjectCreator, MultipleObjectsGenerator):

    def __init__(self, block_width, block_height, field_object_width, field_object_height):
        StaticObjectCreator.__init__(self, block_width, block_height, field_object_width, field_object_height, Coin)
        MultipleObjectsGenerator.__init__(self)


class GhostGenerator(MoveableObjectCreator, MultipleObjectsGenerator):

    def __init__(self, block_width, block_height,
                 field_object_width, field_object_height,
                 horizontal_speed, vertical_speed):
        MoveableObjectCreator.__init__(self, horizontal_speed=horizontal_speed, vertical_speed=vertical_speed,
                                       block_width=block_width, block_height=block_height,
                                       field_object_width=field_object_width, field_object_height=field_object_height,
                                       field_object_type=Ghost)
        MultipleObjectsGenerator.__init__(self)

    def init_images(self, img, img_pos):
        self._images = super().init_images(img, img_pos)