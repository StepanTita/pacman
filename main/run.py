import pygame

from enums import Mode
from model.Objects.Initializer import GameInitializer, EnvironmentInitializer, ObjectsInitializer, DrawerInitializer, \
    FieldInitializer, EventsInitializer

if __name__ == '__main__':

    # Event Initializer
    event_initializer = EventsInitializer()
    event_initializer.init_events()

    # Init environment
    environment_initializer = EnvironmentInitializer()
    screen = environment_initializer.init_screen()

    # Init Objects
    objects_initializer = ObjectsInitializer()
    pacman = objects_initializer.init_pacman()
    ghosts = objects_initializer.init_ghosts()
    walls = objects_initializer.init_walls()

    # Init filed
    field_initializer = FieldInitializer()
    field = field_initializer.init_field()

    # Init drawer
    drawer_initializer = DrawerInitializer()
    drawer = drawer_initializer.init_drawer(screen=screen, pacman=pacman, ghosts=ghosts, walls=walls)

    # Init game
    game_initializer = GameInitializer()
    game = game_initializer.init_game(screen=screen, mode=Mode.PLAY)

    # Set Game
    game.set_screen(screen)
    game.set_field(field)
    game.set_sprites(pacman, ghosts)
    game.set_walls(walls)
    game.set_drawer(drawer)

    pygame.init()
    game.run()
