import pygame

import consts
from enums import Mode
from Controller.Controller import Controller
from Controller.ScreenFieldMapper import ScreenFieldMapper
from model.Events.MoveEvent import PacmanMoveEvent, CoinTossEvent
from model.Game import Game
from model.Objects.Field import Field
from model.Objects.Sprites.Sprite import Pacman
from model.Objects.ObjectsGenerators.ObjectsGenerators import WallGenerator, CoinGenerator
from model.Gameplay.Gameplay import Collider
from view.Drawer import Drawer, SpriteDrawer, ContainerDrawer


class EventsInitializer:

    def init_events(self):
        PacmanMoveEvent.create_event(consts.MOUTH_SPEED)
        CoinTossEvent.create_event(consts.COIN_SPEED)


class FieldInitializer:
    def init_field(self, pacman, ghosts, walls_generator, coins_generator):
        return Field(pacman, ghosts, walls_generator, coins_generator)


class ObjectsInitializer:
    """
    Pattern Factory Method
    """

    def init_pacman(self, img=consts.PACMAN, img_pos=consts.BASE_SPRITE_POS,
                    horizontal_speed=consts.PACMAN_SPEED, vertical_speed=consts.PACMAN_SPEED,
                    x=consts.BLOCK_WIDTH, y=consts.BLOCK_HEIGHT,
                    width=consts.PACMAN_WIDTH, height=consts.PACMAN_HEIGHT):
        return Pacman(img=img, img_pos=img_pos,
                      horizontal_speed=horizontal_speed, vertical_speed=vertical_speed,
                      x=x, y=y,
                      width=width, height=height)

    def init_ghosts(self):
        return ...

    def _init_generator(self, GeneratorType, wall_img, pos_img,
                        block_width, block_height,
                        field_object_width, field_object_height):
        field_objects_generator = GeneratorType(block_width, block_height, field_object_width, field_object_height)
        field_objects_generator.init_images(wall_img, pos_img)
        return field_objects_generator

    def init_walls_generator(self, wall_img=consts.WALLS, pos_img=consts.BASE_WALL_POS,
                             block_width=consts.WALL_WIDTH, block_height=consts.WALL_HEIGHT,
                             field_object_width=consts.WALL_WIDTH, field_object_height=consts.WALL_HEIGHT
                             ):
        walls_generator = self._init_generator(WallGenerator, wall_img, pos_img,
                                               block_width, block_height,
                                               field_object_width, field_object_height)
        return walls_generator

    def init_coins_generator(self, wall_img=consts.COINS, pos_img=consts.BASE_COIN_POS,
                             block_width=consts.BLOCK_WIDTH, block_height=consts.BLOCK_HEIGHT,
                             field_object_width=consts.COIN_WIDTH, field_object_height=consts.COIN_HEIGHT):
        coins_generator = self._init_generator(CoinGenerator, wall_img, pos_img,
                                               block_width, block_height,
                                               field_object_width, field_object_height)
        return coins_generator


class DrawerInitializer:

    def init_drawer(self, screen, field):
        return Drawer(
            screen=screen,
            sprite_drawer=SpriteDrawer(field.get_pacman(), field.get_ghosts()),
            container_drawer=ContainerDrawer(field.get_container())
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
