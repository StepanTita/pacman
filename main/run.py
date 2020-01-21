import pygame

import consts
from enums import Mode
from model.Dependencies.Dependencies import Dependencies
from main.Initializer import GameInitializer, EnvironmentInitializer, ObjectsInitializer, DrawerInitializer, \
    FieldInitializer, EventsInitializer, ColliderInitializer, ScreenFieldMapperInitializer, ControllerInitializer
from model.utils.ImageUtils import FileUtils

if __name__ == '__main__':

    # Event Initializer
    event_initializer = EventsInitializer()
    event_initializer.init_events()

    # Init environment
    environment_initializer = EnvironmentInitializer()
    screen = environment_initializer.init_screen()

    # Init Objects
    objects_initializer = ObjectsInitializer()
    pacman_generator = objects_initializer.init_pacman_generator()
    ghosts_generator = objects_initializer.init_ghosts_generator()
    walls_generator = objects_initializer.init_walls_generator()
    coins_generator = objects_initializer.init_coins_generator()

    # Init field
    rows_count, cols_count, pseudo_field = FileUtils.lines_to_field(Dependencies.load_file(consts.FIELD_NAME))
    field_initializer = FieldInitializer()
    field = field_initializer.init_field(pacman_generator, ghosts_generator, walls_generator, coins_generator)
    field.fill(rows_count=rows_count, cols_count=cols_count, pseudo_field=pseudo_field)

    # Init screen field mapper
    screen_field_mapper_initializer = ScreenFieldMapperInitializer()
    screen_field_mapper = screen_field_mapper_initializer.init_screen_field_mapper(screen, field)

    # Init drawer
    drawer_initializer = DrawerInitializer()
    drawer = drawer_initializer.init_drawer(screen=screen, field=field)

    # Init collider
    collider_initializer = ColliderInitializer()
    collider = collider_initializer.init_collider()

    # Init controller
    controller_initializer = ControllerInitializer()
    controller = controller_initializer.init_controller(collider, screen_field_mapper)

    # Init game
    game_initializer = GameInitializer()
    game = game_initializer.init_game(mode=Mode.PLAY)

    # Set Game
    game.set_drawer(drawer)
    game.set_controller(controller)
    game.set_screen_field_mapper(screen_field_mapper)

    pygame.init()
    game.run()
