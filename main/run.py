import pygame

from enums import Mode
from model.Objects.Initializer import GameInitializer, EnvironmentInitializer, ObjectsInitializer, DrawerInitializer, \
    FieldInitializer, EventsInitializer, ColliderInitializer, ScreenFieldMapperInitializer, ControllerInitializer

if __name__ == '__main__':

    # Event Initializer
    event_initializer = EventsInitializer()
    event_initializer.init_events()

    # Init environment
    environment_initializer = EnvironmentInitializer()
    screen = environment_initializer.init_screen()

    # Init field
    field_initializer = FieldInitializer()
    field = field_initializer.init_field()

    # Init screen field mapper
    screen_field_mapper_initializer = ScreenFieldMapperInitializer()
    screen_field_mapper = screen_field_mapper_initializer.init_screen_field_mapper(screen, field)

    # Init Objects
    objects_initializer = ObjectsInitializer()
    pacman = objects_initializer.init_pacman()
    ghosts = objects_initializer.init_ghosts()
    walls = objects_initializer.init_walls()

    # Init drawer
    drawer_initializer = DrawerInitializer()
    drawer = drawer_initializer.init_drawer(screen=screen, pacman=pacman, ghosts=ghosts, walls=walls)

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
    game.set_sprites(pacman, ghosts)
    game.set_walls(walls)
    game.set_drawer(drawer)
    game.set_controller(controller)

    pygame.init()
    game.run()
