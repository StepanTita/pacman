from itertools import cycle

import pygame
import random

import consts
from enums import Direction
from model.Screen.CustomScreen import ScreenObject
from model.utils.Utils import ImageUtils


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

        self._states = cycle(self._images)
        self._current_state = None

        self._passed_horizontal = 0
        self._passed_vertical = 0

        self.old_moving_direction = None
        self.moving_direction = None

        self.next_state()

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
        self._states = cycle(ImageUtils.rotate_images(self._images, new_dir.value))

    def collide(self, obstacle):
        return self._rect.colliderect(obstacle.get_rect())

    def collidepoint(self, obstacle):
        return self._rect.collidepoint(obstacle.get_middle())

    def discard_move(self):
        self._passed_horizontal -= abs(self._rect.x - self._old_rect.x)
        self._passed_vertical -= abs(self._rect.y - self._old_rect.y)

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
                 width, height, block_width, block_height):
        super().__init__(images, horizontal_speed, vertical_speed, x, y, width, height, block_width, block_height)
        self.update_direction(Direction.RIGHT)
        self._is_invinsible = False
        self._start_time = 0
        self._invinsibility_length = consts.INVINSIBILITY_TIME

    def make_invinsible(self):
        self._is_invinsible = True
        self._start_time = pygame.time.get_ticks()

    def is_invinsible(self):
        return self._is_invinsible

    def check_invinsible(self, end_time):
        if end_time - self._start_time >= self._invinsibility_length:
            self._is_invinsible = False


class Ghost(Sprite):
    def __init__(self, images, horizontal_speed, vertical_speed, x, y,
                 width, height, block_width, block_height):
        super().__init__(images, horizontal_speed + 1, vertical_speed + 1, x, y, width, height, block_width, block_height)
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
            dict = self._dist_euclidian
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


class SleepingGhost(Ghost):
    def __init__(self, images, horizontal_speed, vertical_speed, x, y,
                 width, height, block_width, block_height):
        super().__init__(images, horizontal_speed, vertical_speed, x, y, width, height, block_width, block_height)


class MutantGhost(StupidGhost):
    def __init__(self, images, horizontal_speed, vertical_speed, x, y,
                 width, height, block_width, block_height):
        super().__init__(images, horizontal_speed, vertical_speed, x, y, width * 2, height * 2, block_width, block_height)