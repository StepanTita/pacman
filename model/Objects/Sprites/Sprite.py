from itertools import cycle

import pygame

from enums import Direction
from model.utils.Utils import ImageUtils


def create_history(func):
    def wrapper(self, *args, **kwargs):
        self._old_rect = self._rect.copy()
        result = func(self, *args, **kwargs)
        return result
    return wrapper


class FieldObject(pygame.sprite.Sprite):

    def __init__(self, images, x, y, width, height, block_width, block_height):
        self._images = ImageUtils.resize_images(images,
                                          target_width=width,
                                          target_height=height
                                          )
        pygame.sprite.Sprite.__init__(self)
        # if width < block_width and height < block_height:
        #     self._rect = pygame.Rect(x + width // 2, y + height // 2, width, height)
        # else:
        self._block_width = block_width
        self._block_height = block_height
        self._rect = pygame.Rect(x, y, width, height)
        self._states = cycle([])
        self._current_state = None

    def get_rect(self):
        return self._rect

    def get_width(self):
        return self._rect.width

    def get_height(self):
        return self._rect.height

    def x(self):
        return self._rect.x

    def y(self):
        return self._rect.y

    def current_state(self):
        return self._current_state

    def next_state(self):
        self._current_state = next(self._states)

    def field_x(self):
        return self._rect.x // self.get_width()

    def field_y(self):
        return self._rect.y // self.get_height()


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

    def _dist_manhattan(self, x, y, sprite):
        return abs(sprite.x() - x) + abs(sprite.y() - y)

    def find_sprite(self, sprite):
        distances = [(self._dist_manhattan(self.x() + sprite.speed_horizontal, self.y(), sprite), Direction.RIGHT),
                     (self._dist_manhattan(self.x() - self.speed_horizontal, self.y(), sprite), Direction.LEFT),
                     (self._dist_manhattan(self.x(), self.y() - self.speed_vertical, sprite), Direction.UP),
                     (self._dist_manhattan(self.x(), self.y() + self.speed_vertical, sprite), Direction.DOWN)]
        self._ways = iter([way[1] for way in sorted(distances, key=lambda x: x[0])])

    def next_way(self):
        return next(self._ways)


class SlowGhost(SmartGhost):
    def __init__(self, images, horizontal_speed, vertical_speed, x, y,
                 width, height, block_width, block_height):
        super().__init__(images, horizontal_speed + 1, vertical_speed + 1, x, y, width, height, block_width, block_height)


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