from itertools import cycle

import pygame

from enums import Direction
from model.Dependencies.Dependencies import Dependencies
from model.utils.Utils import ImageUtils


def create_history(func):
    def wrapper(self, *args, **kwargs):
        self._old_rect = self._rect.copy()
        result = func(self, *args, **kwargs)
        return result
    return wrapper


class FieldObject(pygame.sprite.Sprite):

    def __init__(self, images, x, y, width, height):
        self._images = ImageUtils.resize_images(images,
                                          target_width=width,
                                          target_height=height
                                          )
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

    def __init__(self, images, horizontal_speed, vertical_speed, x, y, width, height):
        FieldObject.__init__(self, images, x, y, width, height)

        self._old_rect = None

        self.speed_horizontal = horizontal_speed
        self.speed_vertical = vertical_speed

        self._states = cycle(self._images)
        self._current_state = None

        self.old_moving_direction = None
        self.moving_direction = None

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

    def speed_up(self, times):
        self.speed_horizontal *= times
        self.speed_vertical *= times

    def increase(self, times):
        self._rect.width *= times
        self._rect.height *= times

    def decrease(self, times):
        self._rect.width //= times
        self._rect.height //= times


class Pacman(Sprite):
    def __init__(self, images, horizontal_speed, vertical_speed, x, y,
                 width, height):
        super().__init__(images, horizontal_speed, vertical_speed, x, y, width, height)
        self.update_direction(Direction.RIGHT)


class Ghost(Sprite):
    def __init__(self, images, horizontal_speed, vertical_speed, x, y,
                 width, height):
        super().__init__(images, horizontal_speed, vertical_speed, x, y, width, height)
        count_states = len(self._images) // 4
        self._up = cycle(self._images[:count_states])
        self._right = cycle(self._images[count_states:2 * count_states])
        self._down = cycle(self._images[2 * count_states:3 * count_states])
        self._left = cycle(self._images[3 * count_states:])
        self._states = self._left

    def update_direction(self, new_dir):
        self.moving_direction = new_dir
        if new_dir == Direction.LEFT:
            self._states = self._left
        elif new_dir == Direction.RIGHT:
            self._states = self._right
        elif new_dir == Direction.UP:
            self._states = self._up
        elif new_dir == Direction.DOWN:
            self._states = self._down


class SlowGhost(Ghost):
    def __init__(self, images, horizontal_speed, vertical_speed, x, y,
                 width, height):
        super().__init__(images, horizontal_speed // 2, vertical_speed // 2, x, y, width, height)


class FastGhost(Ghost):
    def __init__(self, images, horizontal_speed, vertical_speed, x, y,
                 width, height):
        super().__init__(images, horizontal_speed * 2, vertical_speed * 2, x, y, width, height)


class SleepingGhost(Ghost):
    def __init__(self, images, horizontal_speed, vertical_speed, x, y,
                 width, height):
        super().__init__(images, horizontal_speed, vertical_speed, x, y, width, height)


class MutantGhost(Ghost):
    def __init__(self, images, horizontal_speed, vertical_speed, x, y,
                 width, height):
        super().__init__(images, horizontal_speed, vertical_speed, x, y, width * 2, height * 2)