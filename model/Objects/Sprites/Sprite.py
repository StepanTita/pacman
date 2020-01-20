from itertools import cycle

import pygame

from enums import Direction
from model.Dependencies.Dependencies import Dependencies
from model.utils.Utils import Utils


def create_history(func):
    def wrapper(self, *args, **kwargs):
        self.old_rect = self.rect.copy()
        result = func(self, *args, **kwargs)
        return result
    return wrapper


class Sprite(pygame.sprite.Sprite):

    def __init__(self, img, img_pos, horizontal_speed, vertical_speed, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.old_rect = None
        self.rect = pygame.Rect(x, y, width, height)

        self._images = Utils.resize_images(
            Utils.crop_image(
                base_img=Dependencies.load_img(img),
                x1=img_pos.x1, x2=img_pos.x2,
                y1=img_pos.y1, y2=img_pos.y2,
                w=img_pos.w, h=img_pos.h
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
        return self.rect.width

    def get_height(self):
        return self.rect.height

    def x(self):
        return self.rect.x

    def y(self):
        return self.rect.y

    @create_history
    def move(self, dx=0, dy=0):
        self.rect.x += dx
        self.rect.y += dy

    @create_history
    def move_to(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y

    def get_sprite_pos(self):
        return self.rect.x, self.rect.y

    def get_sprite_size(self):
        return self.rect.width, self.rect.height

    def current_state(self):
        return self._current_state

    def next_state(self):
        self._current_state = next(self._states)

    def update_direction(self, new_dir):
        self.moving_direction = new_dir
        self._states = cycle(Utils.rotate_images(self._images, new_dir.value))

    def get_rect(self):
        return self.rect

    def collide(self, obstacle):
        return self.rect.colliderect(obstacle.get_rect())

    def discard_move(self):
        self.rect = self.old_rect


class Pacman(Sprite):
    def __init__(self, img, img_pos, horizontal_speed, vertical_speed, x, y,
                 width, height):
        super().__init__(img, img_pos, horizontal_speed, vertical_speed, x, y, width, height)


class Ghost(Sprite):
    def __init__(self, img, img_pos, horizontal_speed, vertical_speed, x, y,
                 width, height):
        super().__init__(img, img_pos, horizontal_speed, vertical_speed, x, y, width, height)
