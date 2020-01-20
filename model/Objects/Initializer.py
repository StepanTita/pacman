import pygame

import consts
from enums import Mode
from model.Events.MoveEvent import PacmanMoveEvent
from model.Game import Game
from model.Objects.Sprites.Sprite import Pacman
from model.Objects.background.Wall import WallGenerator
from view.Drawer import Drawer, SpriteDrawer, WallDrawer


class EventsInitializer:

    def init_events(self):
        PacmanMoveEvent.create_event(consts.MOUTH_SPEED)


class FieldInitializer:
    def init_field(self):
        return ...


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

    def init_walls(self, wall_img=consts.WALLS, img_pos=consts.BASE_WALL_POS,
                   screen_width=consts.SCREEN_WIDTH, screen_height=consts.SCREEN_HEIGHT,
                   block_width=consts.BLOCK_WIDTH, block_height=consts.BLOCK_HEIGHT):
        wall_generator = WallGenerator(wall_img=wall_img, img_pos=img_pos,
                                       screen_width=screen_width, screen_height=screen_height,
                                       block_width=block_width, block_height=block_height)
        wall_generator.generate_frame()

        return wall_generator.get_walls()


class DrawerInitializer:

    def init_drawer(self, screen, pacman, ghosts, walls):
        return Drawer(
            screen=screen,
            sprite_drawer=SpriteDrawer(pacman, ghosts),
            wall_drawer=WallDrawer(walls)
        )


class EnvironmentInitializer:

    def init_screen(self, width=consts.SCREEN_WIDTH, height=consts.SCREEN_HEIGHT):
        return pygame.display.set_mode((width, height))


class GameInitializer:

    def init_game(self, screen, mode=Mode.PLAY):
        return Game(screen_width=screen.get_width(), screen_height=screen.get_height(), mode=mode)
