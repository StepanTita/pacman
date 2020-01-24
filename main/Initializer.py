import pygame

import consts
from enums import Mode
from controller.Controller import Controller
from controller.ScreenFieldMapper import ScreenFieldMapper
from model.Events.MoveEvent import PacmanMoveEvent, CoinTossEvent, GhostAnimEvent
from model.Game import Game
from model.GameStatus.GameStatus import GameStatus
from model.Objects.Field import Field
from model.Objects.GameStatusBlocks.GameStatusBlocks import HealthStatusBlock, StatusText, ScoreStatusBlock, \
    ScoreStatusTextBlock, BonusStatusBlock
from model.Objects.Interactable.Interactable import Rasp, Lemon, Straw, Pear
from model.Objects.ObjectsGenerators.ObjectsGenerators import WallGenerator, CoinGenerator, PacmanGenerator, \
    GhostGenerator, PointGenerator, StrawGenerator, RaspGenerator, LemonGenerator, PearGenerator
from model.Gameplay.Gameplay import Collider
from model.Screen.CustomScreen import CustomScreen
from view.Drawer import Drawer, SpriteDrawer, ContainerDrawer, GhostDrawer, WallDrawer, GameStatusDrawer


class EventsInitializer:

    def init_events(self):
        PacmanMoveEvent.create_event(consts.MOUTH_SPEED)
        CoinTossEvent.create_event(consts.COIN_SPEED)
        GhostAnimEvent.create_event(consts.GHOST_ANIM_SPEED)


class FieldInitializer:
    def init_field(self,
                   pacman_generator,
                   ghosts_generator,
                   walls_generator,
                   coins_generator,
                   points_generator,
                   straw_generator,
                   rasp_generator,
                   lemon_generator,
                   pear_generator):
        return Field(pacman_generator,
                     ghosts_generator,
                     walls_generator,
                     coins_generator,
                     points_generator,
                     straw_generator,
                     rasp_generator,
                     lemon_generator,
                     pear_generator)


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

    def init_points_generator(self, point_img=consts.POINTS, pos_img=consts.BASE_POINT_POS,
                              field_object_width=consts.POINT_WIDTH, field_object_height=consts.POINT_HEIGHT):
        points_generator = self._init_static_generator(PointGenerator, point_img, pos_img,
                                                       field_object_width, field_object_height)
        return points_generator

    def init_straw_generator(self, straw_img=consts.STRAW, pos_img=consts.BASE_STRAW_POS,
                             field_object_width=consts.PACMAN_WIDTH, field_object_height=consts.PACMAN_HEIGHT):
        straw_generator = self._init_static_generator(StrawGenerator, straw_img, pos_img,
                                                      field_object_width, field_object_height)
        return straw_generator

    def init_rasp_generator(self, rasp_img=consts.RASP, pos_img=consts.BASE_RASP_POS,
                            field_object_width=consts.PACMAN_WIDTH, field_object_height=consts.PACMAN_HEIGHT):
        rasp_generator = self._init_static_generator(RaspGenerator, rasp_img, pos_img,
                                                     field_object_width, field_object_height)
        return rasp_generator

    def init_lemon_generator(self, lemon_img=consts.LEMON, pos_img=consts.BASE_LEMON_POS,
                            field_object_width=consts.PACMAN_WIDTH, field_object_height=consts.PACMAN_HEIGHT):
        lemon_generator = self._init_static_generator(LemonGenerator, lemon_img, pos_img,
                                                     field_object_width, field_object_height)
        return lemon_generator

    def init_pear_generator(self, pear_img=consts.PEAR, pos_img=consts.BASE_PEAR_POS,
                            field_object_width=consts.PACMAN_WIDTH, field_object_height=consts.PACMAN_HEIGHT):
        pear_generator = self._init_static_generator(PearGenerator, pear_img, pos_img,
                                                     field_object_width, field_object_height)
        return pear_generator

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

    def _init_health(self, x, y, width, height):
        health_text_block = StatusText(x + width // 16, y + height // 5, width, height, "Health: ")
        health_blocks = [HealthStatusBlock(x + width * (i + 1), y - height // 7, width, height) for i in
                         range(consts.HEALTH)]
        for health_block in health_blocks:
            health_block.init_health_image(heart_img=consts.HEART, heart_pos=consts.BASE_HEART_POS,
                                           empty_heart_img=consts.EHEART, empty_heart_pos=consts.BASE_EHEART_POS)
        return health_blocks, health_text_block

    def _init_score(self, x, y, width, height):
        point_block = ScoreStatusBlock(x, y, width, height)
        point_block.init_image(img=consts.POINTS, img_pos=consts.BASE_POINT_POS)
        point_text_block = ScoreStatusTextBlock(x + width - width // 4, y + height // 7, width, height)
        coin_block = ScoreStatusBlock(x + 2 * width + width // 3, y + height // 4, width // 2, height // 2)
        coin_block.init_image(img=consts.COINS, img_pos=consts.BASE_COIN_POS)
        coin_text_block = ScoreStatusTextBlock(x + 3 * width, y + height // 7, width, height)

        return point_block, point_text_block, coin_block, coin_text_block

    def _init_bonus(self, x, y, width, height):
        rasp_block = BonusStatusBlock(x, y + height // 4, width // 2, height // 2)
        rasp_block.init_image(img=consts.RASP, img_pos=consts.BASE_RASP_POS)
        rasp_block.init_nothing_img(img=consts.CROSS, img_pos=consts.BASE_CROSS_POS)

        lemon_block = BonusStatusBlock(x + width - width // 4, y + height // 4, width // 2, height // 2)
        lemon_block.init_image(img=consts.LEMON, img_pos=consts.BASE_LEMON_POS)
        lemon_block.init_nothing_img(img=consts.CROSS, img_pos=consts.BASE_CROSS_POS)

        straw_block = BonusStatusBlock(x + width + width // 2, y + height // 4, width // 2, height // 2)
        straw_block.init_image(img=consts.STRAW, img_pos=consts.BASE_STRAW_POS)
        straw_block.init_nothing_img(img=consts.CROSS, img_pos=consts.BASE_CROSS_POS)

        pear_block = BonusStatusBlock(x + 2 * width + width // 4, y + height // 4, width // 2, height // 2)
        pear_block.init_image(img=consts.PEAR, img_pos=consts.BASE_PEAR_POS)
        pear_block.init_nothing_img(img=consts.CROSS, img_pos=consts.BASE_CROSS_POS)

        return {Rasp: rasp_block, Lemon: lemon_block, Straw: straw_block, Pear: pear_block}

    def init_gamestatus(self, x, y, width, height):
        health_blocks, health_text_block = self._init_health(x, y, width, height)

        x += (consts.HEALTH + 1) * width + width // 5

        point_block, point_text_block, coin_block, coin_text_block = self._init_score(x, y, width, height)
        x += 4 * width + width // 2 + width // 5

        bonuses = self._init_bonus(x, y, width, height)

        gamestatus = GameStatus(consts.HEALTH,
                                health_blocks, health_text_block,
                                point_block, point_text_block,
                                coin_block, coin_text_block, bonuses)
        return gamestatus


class DrawerInitializer:

    def init_drawer(self, screen, field, gamestatus):
        return Drawer(
            screen=screen,
            sprite_drawer=SpriteDrawer(field.get_pacman()),
            container_drawer=ContainerDrawer(field.get_container()),
            ghost_drawer=GhostDrawer(field.get_ghosts()),
            wall_drawer=WallDrawer(field.get_walls()),
            gamestatus_drawer=GameStatusDrawer(gamestatus)
        )


class EnvironmentInitializer:

    def init_screen(self, width, height, status_height=consts.BLOCK_HEIGHT):
        return CustomScreen(pygame.display.set_mode((width, height + status_height)), status_height)


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
