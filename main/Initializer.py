import pygame

import consts
from enums import Mode
from controller.Controller import Controller
from controller.ScreenFieldMapper import ScreenFieldMapper
from model.Events.MoveEvent import PacmanMoveEvent, CoinTossEvent, GhostAnimEvent
from model.Game import Game
from model.Objects.Field import Field
from model.Objects.ObjectsGenerators.ObjectsGenerators import WallGenerator, CoinGenerator, PacmanGenerator, \
    GhostGenerator
from model.Gameplay.Gameplay import Collider
from view.Drawer import Drawer, SpriteDrawer, ContainerDrawer, GhostDrawer, WallDrawer


class EventsInitializer:

    def init_events(self):
        PacmanMoveEvent.create_event(consts.MOUTH_SPEED)
        CoinTossEvent.create_event(consts.COIN_SPEED)
        GhostAnimEvent.create_event(consts.GHOST_ANIM_SPEED)


class FieldInitializer:
    def init_field(self, pacman_generator, ghosts_generator, walls_generator, coins_generator):
        return Field(pacman_generator, ghosts_generator, walls_generator, coins_generator)


class ObjectsInitializer:
    """
    Pattern Factory Method
    """

    def __init__(self, block_width=consts.BLOCK_WIDTH, block_height=consts.BLOCK_HEIGHT):
        self._block_width = block_width
        self._block_height = block_height

    def _init_static_generator(self, GeneratorType, img, pos_img,
                               field_object_width, field_object_height, split_by=0):
        field_objects_generator = GeneratorType(self._block_width, self._block_height,
                                                field_object_width, field_object_height)
        field_objects_generator.init_images(img, pos_img, split_by)
        field_objects_generator.set_type(0)
        return field_objects_generator

    def init_walls_generator(self, wall_img=consts.WALLS, pos_img=consts.BASE_WALL_POS,
                             field_object_width=consts.WALL_WIDTH, field_object_height=consts.WALL_HEIGHT
                             ):
        walls_generator = self._init_static_generator(WallGenerator, wall_img, pos_img,
                                                      field_object_width, field_object_height)
        return walls_generator

    def init_coins_generator(self, coin_img=consts.COINS, pos_img=consts.BASE_COIN_POS,
                             field_object_width=consts.COIN_WIDTH, field_object_height=consts.COIN_HEIGHT):
        coins_generator = self._init_static_generator(CoinGenerator, coin_img, pos_img,
                                                      field_object_width, field_object_height)
        return coins_generator

    def _init_moveable_generator(self, GeneratorType, img, pos_img,
                                 field_object_width, field_object_height,
                                 horizontal_speed, vertical_speed, split_by=0):
        field_objects_generator = GeneratorType(self._block_width, self._block_height,
                                                field_object_width, field_object_height,
                                                horizontal_speed, vertical_speed)
        field_objects_generator.init_images(img, pos_img, split_by)
        field_objects_generator.set_type(0)
        return field_objects_generator

    def init_pacman_generator(self, pacman_img=consts.PACMAN, pos_img=consts.BASE_SPRITE_POS,
                              horizontal_speed=consts.PACMAN_SPEED, vertical_speed=consts.PACMAN_SPEED,
                              field_object_width=consts.PACMAN_WIDTH, field_object_height=consts.PACMAN_HEIGHT):
        pacman_generator = self._init_moveable_generator(PacmanGenerator,
                                                         pacman_img, pos_img,
                                                         field_object_width, field_object_height,
                                                         horizontal_speed, vertical_speed)
        return pacman_generator

    def init_ghosts_generator(self, ghost_img=consts.GHOSTS, pos_img=consts.BASE_GHOST_POS,
                              horizontal_speed=consts.GHOSTS_SPEED, vertical_speed=consts.GHOSTS_SPEED,
                              field_object_width=consts.GHOST_WIDTH, field_object_height=consts.GHOST_HEIGHT):
        ghosts_generator = self._init_moveable_generator(GhostGenerator,
                                                         ghost_img, pos_img,
                                                         field_object_width, field_object_height,
                                                         horizontal_speed, vertical_speed, split_by=8)
        return ghosts_generator


class DrawerInitializer:

    def init_drawer(self, screen, field):
        return Drawer(
            screen=screen,
            sprite_drawer=SpriteDrawer(field.get_pacman()),
            container_drawer=ContainerDrawer(field.get_container()),
            ghost_drawer=GhostDrawer(field.get_ghosts()),
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
