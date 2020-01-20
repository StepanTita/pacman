import pygame

import consts
from enums import Mode, Direction
from model.Events.MoveEvent import PacmanMoveEvent


class Game:
    def __init__(self, mode):
        self._mode = mode
        self._clock = pygame.time.Clock()

    def set_screen_field_mapper(self, screen_field_mapper):
        self._screen_field_mapper = screen_field_mapper

    def set_walls(self, walls):
        self._walls = walls

    def set_sprites(self, pacman, ghosts):
        self._pacman = pacman
        self._ghosts = ghosts

    def set_drawer(self, drawer):
        self._drawer = drawer

    def set_controller(self, controller):
        self._controller = controller

    def _process_events(self):
        active = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            if event.type == PacmanMoveEvent.get_event_id():
                self._pacman.next_state()
        return active

    def run(self):
        active = True
        while active:
            self._clock.tick(50)

            # Process events
            active = self._process_events()

            # Clear the screen
            self._drawer.clear()

            # Check input
            # Move objects ...
            if self._mode == Mode.AUTO:
                self._controller.auto_game()
            else:
                self._controller.player_game(self._pacman, self._walls)

            # Draw objects ...
            self._drawer.draw()

            # Update the screen
            self._drawer.update()

        pygame.quit()
