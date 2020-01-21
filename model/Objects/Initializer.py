import pygame

import consts
from enums import Mode
from Controller.Controller import Controller
from Controller.ScreenFieldMapper import ScreenFieldMapper
from model.Events.MoveEvent import PacmanMoveEvent
from model.Game import Game
from model.Objects.Field import Field
from model.Objects.Sprites.Sprite import Pacman
from model.Objects.background.Wall import WallGenerator
from model.Gameplay.Gameplay import Collider
from view.Drawer import Drawer, SpriteDrawer, WallDrawer


class EventsInitializer:

    def init_events(self):
        PacmanMoveEvent.create_event(consts.MOUTH_SPEED)


class FieldInitializer:
    def init_field(self, pacman, ghosts, walls_generator):
        return Field(pacman, ghosts, walls_generator)


class ObjectsInitializer:
    """
    Pattern Factory Method
    """

    def init_pacman(self, img=consts.PACMAN, img_pos=consts.BASE_SPRITE_POS,
                    horizontal_speed=consts.PACMAN_SPEED, vertical_speed=consts.PACMAN_SPEED,
                    x=consts.BLOCK_WIDTH, y=consts.BLOCK_HEIGHT,
                    width=consts.BLOCK_WIDTH, height=consts.BLOCK_HEIGHT):
        return Pacman(img=img, img_pos=img_pos,
                      horizontal_speed=horizontal_speed, vertical_speed=vertical_speed,
                      x=x, y=y,
                      width=width, height=height)

    def init_ghosts(self):
        return ...

    def init_walls_generator(self, wall_img=consts.WALLS, pos_img=consts.BASE_WALL_POS,
                             block_width=consts.BLOCK_WIDTH, block_height=consts.BLOCK_HEIGHT):
        walls_generator = WallGenerator(block_width, block_height)
        walls_generator.init_images(wall_img, pos_img, block_width, block_height)
        return walls_generator


class DrawerInitializer:

    def init_drawer(self, screen, field):
        return Drawer(
            screen=screen,
            sprite_drawer=SpriteDrawer(field.get_pacman(), field.get_ghosts()),
            wall_drawer=WallDrawer(field.get_walls())
        )


class EnvironmentInitializer:

    def init_screen(self, width=consts.SCREEN_WIDTH, height=consts.SCREEN_HEIGHT):
        return pygame.display.set_mode((width, height))


class GameInitializer:

    def init_game(self, mode=Mode.PLAY):
        return Game(mode=mode)


class ColliderInitializer:

    def init_collider(self):
        return Collider()


class ControllerInitializer:

    def init_controller(self, collider, screen_field_mapper):
        return Controller(collider, screen_field_mapper)


class ScreenFieldMapperInitializer:

    def init_screen_field_mapper(self, screen, field):
        screen_field_mapper = ScreenFieldMapper(screen, field)
        return screen_field_mapper
