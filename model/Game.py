import pygame

import consts
from enums import Mode, Direction
from model.Events.MoveEvent import PacmanMoveEvent


class Game:
    def __init__(self, screen_width, screen_height, mode):
        self._mode = mode
        self._clock = pygame.time.Clock()

    def set_screen(self, screen):
        self._screen = screen

    def set_field(self, field):
        self._field = field

    def set_walls(self, walls):
        self._walls = walls

    def set_sprites(self, pacman, ghosts):
        self._pacman = pacman
        self._ghosts = ghosts

    def set_drawer(self, drawer):
        self._drawer = drawer

    def _auto_game(self):
        ...  # TODO

    def _player_game(self):
        keyinput = pygame.key.get_pressed()

        if keyinput[pygame.K_LEFT] and self._pacman.x() > 0:
            if self._pacman.moving_direction != Direction.RIGHT:
                self._pacman.update_direction(Direction.RIGHT)
            self._pacman.move(dx=-self._pacman.speed_horizontal)
        elif keyinput[pygame.K_RIGHT] and self._pacman.x() < consts.SCREEN_WIDTH - self._pacman.get_width():
            if self._pacman.moving_direction != Direction.LEFT:
                self._pacman.update_direction(Direction.LEFT)
            self._pacman.move(dx=self._pacman.speed_horizontal)
        elif keyinput[pygame.K_UP] and self._pacman.y() > 0:
            if self._pacman.moving_direction != Direction.UP:
                self._pacman.update_direction(Direction.UP)
            self._pacman.move(dy=-self._pacman.speed_vertical)
        elif keyinput[pygame.K_DOWN] and self._pacman.y() < consts.SCREEN_HEIGHT - self._pacman.get_height():
            if self._pacman.moving_direction != Direction.BOT:
                self._pacman.update_direction(Direction.BOT)
            self._pacman.move(dy=self._pacman.speed_vertical)

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
                self._auto_game()
            else:
                self._player_game()

            # Draw objects ...
            self._drawer.draw()

            # Update the screen
            self._drawer.update()

        pygame.quit()
