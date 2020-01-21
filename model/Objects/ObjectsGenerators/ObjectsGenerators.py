from pygame.sprite import Group

from model.Dependencies.Dependencies import Dependencies
from model.Objects.Interactable.Interactable import Coin
from model.Objects.background.Wall import Wall
from model.utils.ImageUtils import ImageUtils


class ObjectGenerator:
    def __init__(self, block_width, block_height,
                 field_object_width, field_object_height, field_object_type):
        self._block_width = block_width
        self._block_height = block_height
        self._field_object_width = field_object_width
        self._field_object_height = field_object_height
        self._container = Group()
        self._field_object_type = field_object_type

    def init_images(self, wall_img, img_pos):
        self._images = ImageUtils.resize_images(
            ImageUtils.crop_image(
                base_img=Dependencies.load_img(wall_img),
                img_pos=img_pos
            ), target_width=self._field_object_width, target_height=self._field_object_height
        )

    def _add(self, field_object):
        self._container.add(field_object)

    def create(self, row, col):
        return self._field_object_type(images=self._images,
                                      x=col * self._block_width, y=row * self._block_height,
                                      width=self._field_object_width, height=self._field_object_height)

    def generate(self, field):
        for i in range(field.rows_count):
            for j in range(field.cols_count):
                if type(field[i][j]) is self._field_object_type:
                    self._add(field[i][j])

    def get_field_objects(self):
        return self._container


class WallGenerator(ObjectGenerator):
    """
    Builder Pattern
    """

    def __init__(self, block_width, block_height, field_object_width, field_object_height, ):
        ObjectGenerator.__init__(self, block_width, block_height, field_object_width, field_object_height, Wall)

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


class CoinGenerator(ObjectGenerator):

    def __init__(self, block_width, block_height, field_object_width, field_object_height, ):
        ObjectGenerator.__init__(self, block_width, block_height, field_object_width, field_object_height, Coin)
