from itertools import cycle

import pygame
from pygame.sprite import Group

from model.Dependencies.Dependencies import Dependencies
from model.Objects.Sprites.Sprite import FieldObject
from model.utils.ImageUtils import ImageUtils


class Wall(FieldObject):

    def __init__(self, images, x, y, width, height):
        FieldObject.__init__(self, x, y, width, height)

        self._images = images
        self._states = cycle(self._images)
        self._current_state = None

        self.next_state()


class WallGenerator:
    """
    Builder Pattern
    """

    def __init__(self, block_width, block_height):
        self._walls = Group()
        self.block_width = block_width
        self.block_height = block_height

    def init_images(self, wall_img, img_pos, block_width, block_height):
        self._images = ImageUtils.resize_images(
            ImageUtils.crop_image(
                base_img=Dependencies.load_img(wall_img),
                img_pos=img_pos
            ), target_width=block_width, target_height=block_height
        )

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

    def create_wall(self, row, col):
        return Wall(images=self._images, x=col * self.block_width, y=row * self.block_height,
                    width=self.block_width, height=self.block_height)

    def generate_walls(self, field):
        for i in range(field.rows_count):
            for j in range(field.cols_count):
                if type(field[i][j]) is Wall:
                    self._walls.add(field[i][j])

    def get_walls(self):
        return self._walls
