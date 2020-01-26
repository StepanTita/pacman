from itertools import cycle

import pygame
import random

from pygame.surface import Surface

import consts
from enums import Direction
from model.Dependencies.Dependencies import Dependencies
from model.Screen.CustomScreen import ScreenObject
from model.utils.Utils import ImageUtils
from view.Color import Color


def create_history(func):
    def wrapper(self, *args, **kwargs):
        self._old_rect = self._rect.copy()
        result = func(self, *args, **kwargs)
        return result
    return wrapper


class FieldObject(ScreenObject):

    def __init__(self, images, x, y, width, height, block_width, block_height):
        ScreenObject.__init__(self, x, y, width, height)
        self._images = ImageUtils.resize_images(images,
                                          target_width=width,
                                          target_height=height
                                          )

        self._block_width = block_width
        self._block_height = block_height

        self._img_states = self._images
        self._states = cycle(self._images)
        self._current_state = None

        self.next_state()

    def current_state(self):
        return self._current_state

    def next_state(self):
        self._current_state = next(self._states)

    def get_middle(self):
        return self._rect.center


class MiddledFieldObject(FieldObject):
    def __init__(self, images, x, y, width, height, block_width, block_height):
        super().__init__(images, x, y, width, height, block_width, block_height)
        if width < block_width and height < block_height:
            self._rect = pygame.Rect(x + width // 2, y + height // 2, width, height)
        else:
            self._rect = pygame.Rect(x, y, width, height)


class Sprite(FieldObject):

    def __init__(self, images, horizontal_speed, vertical_speed, x, y, width, height, block_width, block_height):
        FieldObject.__init__(self, images, x, y, width, height, block_width, block_height)

        self._old_rect = None

        self.speed_horizontal = horizontal_speed
        self.speed_vertical = vertical_speed

        self._passed_horizontal = 0
        self._passed_vertical = 0

        self.old_moving_direction = None
        self.moving_direction = None

    @create_history
    def move(self, dx=0, dy=0):
        self._rect.x += dx
        self._rect.y += dy

        self._passed_horizontal += abs(dx)
        self._passed_vertical += abs(dy)

    @create_history
    def move_to(self, new_x, new_y):
        self._rect.x = new_x
        self._rect.y = new_y

        self._passed_horizontal += abs(self._rect.x - new_x)
        self._passed_vertical += abs(self._rect.y - new_y)

    def get_sprite_pos(self):
        return self._rect.x, self._rect.y

    def get_sprite_size(self):
        return self._rect.width, self._rect.height

    def update_direction(self, new_dir):
        self.moving_direction = new_dir
        self._states = cycle(ImageUtils.rotate_images(self._img_states, new_dir.value))

    def collide(self, obstacle):
        return self._rect.colliderect(obstacle.get_rect())

    def collidepoint(self, obstacle):
        return self._rect.collidepoint(obstacle.get_middle())

    def discard_move(self):
        self._passed_horizontal -= abs(self._rect.x - self._old_rect.x)
        self._passed_vertical -= abs(self._rect.y - self._old_rect.y)

        self._rect = self._old_rect


class Pacman(Sprite):
    def __init__(self, images, horizontal_speed, vertical_speed, x, y,
                 width, height, block_width, block_height):
        super().__init__(images, horizontal_speed, vertical_speed, x, y, width, height, block_width, block_height)
        self.update_direction(Direction.RIGHT)

        self._is_invinsible = False
        self._speeded = False
        self._breaker = False

        self._invinsibility_length = consts.INVINSIBILITY_TIME
        self._speed_length = consts.SPEED_TIME
        self._breaker_length = consts.BREAKER_TIME

        self._inv_start_time = 0
        self._speed_start_time = 0
        self._break_start_time = 0

    def _read_image(self, img=consts.PACMAN, img_pos=consts.ALL_SPRITE_POS):
        return ImageUtils.resize_images(
            ImageUtils.crop_image(
                base_img=Dependencies.load_img(img),
                img_pos=img_pos
            ),
            target_width=self.get_width(),
            target_height=self.get_height()
        )

    def is_invinsible(self):
        return self._is_invinsible

    def is_speeded(self):
        return self._speeded

    def is_breaker(self):
        return self._breaker

    def make_invinsible(self):
        self._is_invinsible = True

        self._img_states = self._read_image()
        self._states = cycle(self._img_states)
        self.update_direction(self.moving_direction)
        self._inv_start_time = pygame.time.get_ticks()

    def make_breaker(self):
        self._breaker = True
        self.speed_down()
        self._break_start_time = pygame.time.get_ticks()

    def make_speed(self):
        self._speeded = True
        self.speed_up()
        self._speed_start_time = pygame.time.get_ticks()

    def speed_up(self, times=2):
        self.speed_horizontal *= times
        self.speed_vertical *= times

    def speed_down(self, times=2):
        self.speed_horizontal //= times
        self.speed_vertical //= times

    def check_invinsible(self, end_time):
        if end_time - self._inv_start_time >= self._invinsibility_length:
            self._is_invinsible = False
            self._img_states = self._images
            self._states = cycle(self._img_states)
            self.update_direction(self.moving_direction)

    def check_speed(self, end_time):
        if end_time - self._speed_start_time >= self._speed_length:
            self._speeded = False
            self.speed_down()

    def check_breaker(self, end_time):
        if end_time - self._break_start_time >= self._breaker_length:
            self._breaker = False
            self.speed_up()


class Ghost(Sprite):
    def __init__(self, images, horizontal_speed, vertical_speed, x, y,
                 width, height, block_width, block_height):
        super().__init__(images, horizontal_speed, vertical_speed, x, y, width, height, block_width, block_height)
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


class StupidGhost(Ghost):
    def __init__(self, images, horizontal_speed, vertical_speed, x, y, width, height, block_width, block_height):
        super().__init__(images, horizontal_speed, vertical_speed, x, y, width, height, block_width, block_height)
        self._current_step = None
        self._instructions = None

    def set_instructions(self, instructions):
        self._instructions = cycle(instructions)
        self._current_step = next(self._instructions)

    def current_step(self):
        if self._passed_horizontal >= self._block_width:
            self._passed_horizontal = 0
            self.next_step()
        elif self._passed_vertical >= self._block_height:
            self._passed_vertical = 0
        return self._current_step

    def next_step(self):
        self._current_step = next(self._instructions)


class SmartGhost(Ghost):
    def __init__(self, images, horizontal_speed, vertical_speed, x, y, width, height, block_width, block_height):
        super().__init__(images, horizontal_speed, vertical_speed, x, y, width, height, block_width, block_height)
        self._ways = iter([])
        self._prev_step = None
        self._counter = {Direction.LEFT: Direction.RIGHT,
                         Direction.RIGHT: Direction.LEFT,
                         Direction.UP: Direction.DOWN,
                         Direction.DOWN: Direction.UP}

    def _dist_manhattan(self, x, y, sprite):
        return abs(sprite.x() - x) + abs(sprite.y() - y)

    def _dist_euclidian(self, x, y, sprite):
        x1 = sprite.x() - x
        y1 = sprite.y() - y
        return x1**2 + y1**2

    def find_sprite(self, sprite):
        dist = self._dist_manhattan
        if random.randint(0, 1):
            dist = self._dist_euclidian
        distances = [(dist(self.x() + sprite.speed_horizontal, self.y(), sprite), Direction.RIGHT),
                     (dist(self.x() - self.speed_horizontal, self.y(), sprite), Direction.LEFT),
                     (dist(self.x(), self.y() - self.speed_vertical, sprite), Direction.UP),
                     (dist(self.x(), self.y() + self.speed_vertical, sprite), Direction.DOWN)]
        ways = [way[1] for way in sorted(distances, key=lambda x: x[0]) if way[1] != self._prev_step]
        self._ways = iter(ways)

    def next_step(self):
        next_step = next(self._ways)
        self._prev_step = self._counter[next_step]
        return next_step


class SlowGhost(SmartGhost):
    def __init__(self, images, horizontal_speed, vertical_speed, x, y,
                 width, height, block_width, block_height):
        super().__init__(images, horizontal_speed, vertical_speed, x, y, width, height, block_width, block_height)


class FastGhost(StupidGhost):
    def __init__(self, images, horizontal_speed, vertical_speed, x, y,
                 width, height, block_width, block_height):
        super().__init__(images, horizontal_speed * 2, vertical_speed * 2, x, y, width, height, block_width, block_height)


class SleepingGhost(SmartGhost):
    def __init__(self, images, horizontal_speed, vertical_speed, x, y,
                 width, height, block_width, block_height):
        super().__init__(images, horizontal_speed, vertical_speed, x, y, width, height, block_width, block_height)

        images = self._read_image()
        self._left = cycle([images[0]])
        self._right = cycle([images[1]])

    def _read_image(self, img=consts.GHOSTS, img_pos=consts.BASE_INV_POS):
        return ImageUtils.resize_images(
            ImageUtils.crop_image(
                base_img=Dependencies.load_img(img),
                img_pos=img_pos
            ),
            target_width=self.get_width(),
            target_height=self.get_height()
        )


class MutantGhost(StupidGhost):
    def __init__(self, images, horizontal_speed, vertical_speed, x, y,
                 width, height, block_width, block_height):
        super().__init__(images, horizontal_speed, vertical_speed, x, y, width * 2, height * 2, block_width, block_height)
