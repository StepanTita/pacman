import pygame

import consts
from enums import Mode
from model.Dependencies.Dependencies import Dependencies
from main.Initializer import GameInitializer, EnvironmentInitializer, ObjectsInitializer, DrawerInitializer, \
    FieldInitializer, EventsInitializer, ColliderInitializer, ScreenFieldMapperInitializer, ControllerInitializer
from model.utils.Utils import FileUtils, BaseUtils


def main():
    pygame.font.init()

    # Event Initializer
    event_initializer = EventsInitializer()
    event_initializer.init_events()

    # Init environment
    rows_count, cols_count, pseudo_field = FileUtils.lines_to_field(Dependencies.load_file(consts.FIELD_NAME))
    environment_initializer = EnvironmentInitializer()
    screen = environment_initializer.init_screen(width=consts.BLOCK_WIDTH * cols_count,
                                                 height=consts.BLOCK_HEIGHT * rows_count)

    # Init Objects
    objects_initializer = ObjectsInitializer()
    pacman_generator = objects_initializer.init_pacman_generator()
    ghosts_generator = objects_initializer.init_ghosts_generator()
    walls_generator = objects_initializer.init_walls_generator()
    coins_generator = objects_initializer.init_coins_generator()
    points_generator = objects_initializer.init_points_generator()

    # Init field
    field_initializer = FieldInitializer()
    field = field_initializer.init_field(pacman_generator, ghosts_generator, walls_generator, coins_generator, points_generator)
    field.fill(rows_count=rows_count, cols_count=cols_count, pseudo_field=pseudo_field)
    field.set_instructions(
        BaseUtils.create_instructions(fast_ghost=Dependencies.load_instructions(path=consts.FAST_INSTRUCTIONS),
                                      mutant_ghost=Dependencies.load_instructions(path=consts.MUTANT_INSTRUCTIONS))
    )

    # Init screen field mapper
    screen_field_mapper_initializer = ScreenFieldMapperInitializer()
    screen_field_mapper = screen_field_mapper_initializer.init_screen_field_mapper(screen, field)

    gamestatus = objects_initializer.init_gamestatus(x=screen_field_mapper.left_screen_border(), y=screen_field_mapper.down_screen_border(),
                                                     width=consts.BLOCK_WIDTH, height=consts.BLOCK_HEIGHT)

    # Init drawer
    drawer_initializer = DrawerInitializer()
    drawer = drawer_initializer.init_drawer(screen=screen, field=field, gamestatus=gamestatus)

    # Init collider
    collider_initializer = ColliderInitializer()
    collider = collider_initializer.init_collider()

    # Init controller
    controller_initializer = ControllerInitializer()
    controller = controller_initializer.init_controller(collider, screen_field_mapper)
    controller.set_gamestatus(gamestatus)

    # Init game
    game_initializer = GameInitializer()
    game = game_initializer.init_game(mode=Mode.PLAY)

    # Set Game
    game.set_drawer(drawer)
    game.set_controller(controller)
    game.set_screen_field_mapper(screen_field_mapper)

    pygame.init()
    game.run()


def test():
    import random as rd
    SIZE_X = 720
    SIZE_Y = 480
    STEP = 5

    q_table = {}
    for x1 in range(-SIZE_X + 1, SIZE_X, STEP):
        for y1 in range(-SIZE_Y + 1, SIZE_Y, STEP):
            for x2 in range(-SIZE_X + 1, SIZE_X, STEP):
                for y2 in range(-SIZE_Y + 1, SIZE_Y, STEP):
                    q_table[((x1, y1), (x2, y2))] = rd.randint(-5, 0)


if __name__ == '__main__':
    main()
