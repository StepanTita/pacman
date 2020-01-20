import pygame

from enums import Direction


class Controller:

    def __init__(self, collider, screen_field_mapper):
        self._left = None
        self._right = None
        self._up = None
        self._down = None
        self._collider = collider
        self._screen_field_mapper = screen_field_mapper

    def _update_buttons(self):
        keyinput = pygame.key.get_pressed()

        self._left = keyinput[pygame.K_LEFT]
        self._right = keyinput[pygame.K_RIGHT]
        self._up = keyinput[pygame.K_UP]
        self._down = keyinput[pygame.K_DOWN]

    def _any_control_key_pressed(self):
        return self._left or self._right or self._up or self._down

    def _can_move_left(self, sprite):
        left_border = self._screen_field_mapper.left_screen_border()
        return self._left and sprite.x() > left_border

    def _can_move_right(self, sprite):
        right_border = self._screen_field_mapper.right_screen_border() - sprite.get_width()
        return self._right and sprite.x() < right_border

    def _can_move_up(self, sprite):
        up_border = self._screen_field_mapper.up_screen_border()
        return self._up and sprite.y() > up_border

    def _can_move_down(self, sprite):
        down_border = self._screen_field_mapper.down_screen_border() - sprite.get_height()
        return self._down and sprite.y() < down_border

    def _move_left(self, sprite):
        if sprite.moving_direction != Direction.LEFT:
            sprite.update_direction(Direction.LEFT)
        sprite.move(dx=-sprite.speed_horizontal)

    def _move_right(self, sprite):
        if sprite.moving_direction != Direction.RIGHT:
            sprite.update_direction(Direction.RIGHT)
        sprite.move(dx=sprite.speed_horizontal)

    def _move_up(self, sprite):
        if sprite.moving_direction != Direction.UP:
            sprite.update_direction(Direction.UP)
        sprite.move(dy=-sprite.speed_vertical)

    def _move_down(self, sprite):
        if sprite.moving_direction != Direction.BOT:
            sprite.update_direction(Direction.BOT)
        sprite.move(dy=sprite.speed_vertical)

    def _move(self, sprite):

        if self._can_move_left(sprite):
            self._move_left(sprite)
        elif self._can_move_right(sprite):
            self._move_right(sprite)
        elif self._can_move_up(sprite):
            self._move_up(sprite)
        elif self._can_move_down(sprite):
            self._move_down(sprite)

    def auto_game(self):
        ...  # TODO

    def player_game(self, sprite, obstacles):
        self._update_buttons()
        if self._any_control_key_pressed():
            self._move(sprite)
            collided = self._collider.check_collisions(sprite, obstacles)
            if collided:
                sprite.discard_move()
        return