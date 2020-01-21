from itertools import cycle

import pygame

from enums import Direction
from model.Dependencies.Dependencies import Dependencies
from model.utils.ImageUtils import ImageUtils


def create_history(func):
    def wrapper(self, *args, **kwargs):
        self._old_rect = self._rect.copy()
        result = func(self, *args, **kwargs)
        return result
    return wrapper


class FieldObject(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self._rect = pygame.Rect(x, y, width, height)
        self._states = cycle([])
        self._current_state = None

    def get_rect(self):
        return self._rect

    def current_state(self):
        return self._current_state

    def next_state(self):
        self._current_state = next(self._states)


class Sprite(FieldObject):

    def __init__(self, img, img_pos, horizontal_speed, vertical_speed, x, y, width, height):
        FieldObject.__init__(self, x, y, width, height)

        self._old_rect = None

        self._images = ImageUtils.resize_images(
            ImageUtils.crop_image(
                base_img=Dependencies.load_img(img),
                img_pos=img_pos
            ), target_width=width, target_height=height
        )

        self.speed_horizontal = horizontal_speed
        self.speed_vertical = vertical_speed

        self._states = cycle(self._images)
        self._current_state = None

        self.old_moving_direction = None
        self.moving_direction = None
        self.update_direction(Direction.RIGHT)

        self.next_state()

    def get_width(self):
        return self._rect.width

    def get_height(self):
        return self._rect.height

    def x(self):
        return self._rect.x

    def y(self):
        return self._rect.y

    @create_history
    def move(self, dx=0, dy=0):
        self._rect.x += dx
        self._rect.y += dy

    @create_history
    def move_to(self, new_x, new_y):
        self._rect.x = new_x
        self._rect.y = new_y

    def get_sprite_pos(self):
        return self._rect.x, self._rect.y

    def get_sprite_size(self):
        return self._rect.width, self._rect.height

    def current_state(self):
        return self._current_state

    def next_state(self):
        self._current_state = next(self._states)

    def update_direction(self, new_dir):
        self.moving_direction = new_dir
        self._states = cycle(ImageUtils.rotate_images(self._images, new_dir.value))

    def get_rect(self):
        return self._rect

    def collide(self, obstacle):
        return self._rect.colliderect(obstacle.get_rect())

    def discard_move(self):
        self._rect = self._old_rect


class Pacman(Sprite):
    def __init__(self, img, img_pos, horizontal_speed, vertical_speed, x, y,
                 width, height):
        super().__init__(img, img_pos, horizontal_speed, vertical_speed, x, y, width, height)


class Ghost(Sprite):
    def __init__(self, img, img_pos, horizontal_speed, vertical_speed, x, y,
                 width, height):
        super().__init__(img, img_pos, horizontal_speed, vertical_speed, x, y, width, height)
