from itertools import cycle

import pygame
from pygame.sprite import Group

from model.dependencies.Dependencies import Dependencies
from model.utils.Utils import Utils


class Wall(pygame.sprite.Sprite):

    def __init__(self, images, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(x, y, width, height)

        self._images = images
        self._states = cycle(self._images)
        self._current_state = None

        self.next_state()

    def get_rect(self):
        return self.rect

    def current_state(self):
        return self._current_state

    def next_state(self):
        self._current_state = next(self._states)


class WallGenerator:
    """
    Builder Pattern
    """

    def __init__(self, wall_img, img_pos,
                 screen_width, screen_height,
                 block_width, block_height):

        self._images = Utils.resize_images(
            Utils.crop_image(
                base_img=Dependencies.load_img(wall_img),
                x1=img_pos.x1, x2=img_pos.x2,
                y1=img_pos.y1, y2=img_pos.y2
            ), target_width=block_width, target_height=block_height
        )
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._block_width = block_width
        self._block_height = block_height
        self._walls = Group()

    def generate_walls(self, x1, y1, x2, y2):
        for i in range(x1, x2):
            for j in range(y1, y2):
                self._walls.add(Wall(images=self._images, x=i * self._block_width, y=j * self._block_height,
                                     width=self._block_width, height=self._block_height))

    def generate_frame(self):
        self.generate_walls(x1=0, x2=self._screen_width // self._block_width,
                            y1=0, y2=1)
        self.generate_walls(x1=0, x2=self._screen_width // self._block_width,
                            y1=self._screen_height // self._block_height, y2=self._screen_height // self._block_height + 1)
        self.generate_walls(x1=0, x2=1,
                            y1=0, y2=self._screen_height // self._block_height)
        self.generate_walls(x1=self._screen_width // self._block_width, x2=self._screen_width // self._block_width + 1,
                            y1=0, y2=self._screen_height // self._block_height)

    def get_walls(self):
        return self._walls
