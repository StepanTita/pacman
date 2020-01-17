from itertools import cycle

import pygame

from enums import Direction
from model.dependencies.Dependencies import Dependencies
from model.utils.Utils import Utils


class Sprite(pygame.sprite.Sprite):
    def __init__(self, img, img_pos, speed, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(x, y, width, height)

        self._images = Utils.resize_images(
            Utils.crop_image(
                base_img=Dependencies.load_img(img),
                x1=img_pos.x1, x2=img_pos.x2,
                y1=img_pos.y1, y2=img_pos.y2
            ), target_width=width, target_height=height
        )

        self.speed = speed

        self._states = cycle(self._images)
        self._current_state = None

        self.moving_direction = None
        self.update_direction(Direction.LEFT)

        self.next_state()

    def move(self, dx=0, dy=0):
        self.rect.x += dx
        self.rect.y += dy

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


class Pacman(Sprite):
    def __init__(self, img, img_pos, speed,
                 x, y,
                 width, height):
        super().__init__(img, img_pos, speed, x, y, width, height)


class Ghost(Sprite):
    def __init__(self, img, img_pos, speed,
                 x, y,
                 width, height):
        super().__init__(img, img_pos, speed, x, y, width, height)
