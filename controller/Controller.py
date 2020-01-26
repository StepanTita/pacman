import pygame

from enums import Direction
from model.Objects.Interactable.Interactable import Coin, Point, Pear, Rasp, Lemon, Straw
from model.Objects.Sprites.Sprite import StupidGhost, SmartGhost, Ghost
from model.Objects.background.Wall import Wall


class Controller:

    def __init__(self, collider, screen_field_mapper):
        self._left = None
        self._right = None
        self._up = None
        self._down = None
        self._collider = collider
        self._screen_field_mapper = screen_field_mapper

        self._paused = False

    def set_gamestatus(self, gamestatus):
        self._gamestatus = gamestatus

    def _update_buttons(self):
        keyinput = pygame.key.get_pressed()

        self._left = keyinput[pygame.K_LEFT]
        self._right = keyinput[pygame.K_RIGHT]
        self._up = keyinput[pygame.K_UP]
        self._down = keyinput[pygame.K_DOWN]

        pause = keyinput[pygame.K_p]
        if pause:
            self._paused = not self._paused

    def is_paused(self):
        self._update_buttons()
        return self._paused

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
        if sprite.moving_direction != Direction.DOWN:
            sprite.update_direction(Direction.DOWN)
        sprite.move(dy=sprite.speed_vertical)

    def _move_sprite(self, sprite):
        if self._can_move_left(sprite):
            self._move_left(sprite)
        elif self._can_move_right(sprite):
            self._move_right(sprite)
        elif self._can_move_up(sprite):
            self._move_up(sprite)
        elif self._can_move_down(sprite):
            self._move_down(sprite)

    def _move_ghost(self, ghost, next_step):
        if next_step == Direction.LEFT:
            self._move_left(ghost)
        elif next_step == Direction.RIGHT:
            self._move_right(ghost)
        elif next_step == Direction.UP:
            self._move_up(ghost)
        elif next_step == Direction.DOWN:
            self._move_down(ghost)

    def is_gameover(self):
        return self._gamestatus.is_gameover()

    def score(self):
        return self._gamestatus.score()

    def auto_game(self):
        ...  # TODO

    def player_game(self, sprite, obstacles):
        self._update_buttons()
        if self._any_control_key_pressed():
            self._move_sprite(sprite)
            collision = self._collider.check_player_collisions(sprite, obstacles)
            if type(collision) is Wall:
                if sprite.is_breaker():
                    obstacles.remove(collision)
                else:
                    sprite.discard_move()
            return type(collision) is Wall
        return False

    def player_game_group(self, sprite, groups):
        if self._any_control_key_pressed():
            for obstacles in groups:
                #self._move_sprite(sprite)
                collision = self._collider.check_player_collisions(sprite, obstacles)

                if type(collision) is Coin:
                    obstacles.remove(collision)
                    self._screen_field_mapper.coin_found()
                    self._gamestatus.update_coins_score()
                elif type(collision) is Point:
                    obstacles.remove(collision)
                    self._screen_field_mapper.point_found()
                    self._gamestatus.update_points_score()
                elif type(collision) is Pear:
                    obstacles.remove(collision)
                    self._gamestatus.update_bonuses(Pear)
                    sprite.make_invinsible()
                elif type(collision) is Rasp:
                    obstacles.remove(collision)
                    self._gamestatus.update_bonuses(Rasp)
                    sprite.make_speed()
                elif type(collision) is Lemon:
                    obstacles.remove(collision)
                    self._gamestatus.update_bonuses(Lemon)
                    sprite.make_breaker()
                elif type(collision) is Straw:
                    obstacles.remove(collision)
                    self._gamestatus.update_bonuses(Straw)
                    self._gamestatus.increase_health()

    def stupid_ghosts(self, ghosts, obstacles):
        for ghost in ghosts:
            if issubclass(type(ghost), StupidGhost):
                self._move_ghost(ghost, ghost.current_step())
            collided = self._collider.check_ghost_collisions(ghost, obstacles)
            if collided:
                ghost.discard_move()
                ghost.next_step()

    def smart_ghosts(self, sprite, ghosts, obstacles):
        for ghost in ghosts:
            if issubclass(type(ghost), SmartGhost):
                collided = True
                ghost.find_sprite(sprite)
                while collided:
                    self._move_ghost(ghost, ghost.next_step())
                    collided = self._collider.check_ghost_collisions(ghost, obstacles)
                    if not collided:
                        break
                    ghost.discard_move()

    def ghosts_player(self, sprite, ghosts):
        collision = self._collider.check_player_collisions(sprite, ghosts)
        if issubclass(type(collision), Ghost) and not sprite.is_invinsible():
            sprite.make_invinsible()
            self._gamestatus.decrease_health()
