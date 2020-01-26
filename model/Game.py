import pygame

import consts
from enums import Mode
from model.Events.MoveEvent import PacmanMoveEvent, CoinTossEvent, GhostAnimEvent


class Game:
    def __init__(self, mode):
        self._mode = mode
        self._clock = pygame.time.Clock()

    def set_screen_field_mapper(self, screen_field_mapper):
        self._screen_field_mapper = screen_field_mapper

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
                self._screen_field_mapper.get_pacman().next_state()
            elif event.type == CoinTossEvent.get_event_id():
                self._screen_field_mapper.change_coins_state()
            elif event.type == GhostAnimEvent.get_event_id():
                self._screen_field_mapper.change_ghosts_state()
        return active

    def _check_invincible(self):
        pacman = self._screen_field_mapper.get_pacman()
        if pacman.is_invinsible():
            end_time = pygame.time.get_ticks()
            pacman.check_invinsible(end_time)

    def _check_speed(self):
        pacman = self._screen_field_mapper.get_pacman()
        if pacman.is_speeded():
            end_time = pygame.time.get_ticks()
            pacman.check_speed(end_time)

    def _check_breaker(self):
        pacman = self._screen_field_mapper.get_pacman()
        if pacman.is_breaker():
            end_time = pygame.time.get_ticks()
            pacman.check_breaker(end_time)

    def _check_statuses(self):
        self._check_invincible()
        self._check_speed()
        self._check_breaker()

    def _check_gameover(self):
        if self._screen_field_mapper.is_victory():
            self._drawer.draw_victory()
            return True
        elif self._controller.is_gameover():
            self._drawer.draw_gameover(self._controller.score())
            return True
        return False

    def _player_game(self):
        if not self._controller.player_game(self._screen_field_mapper.get_pacman(),
                                            self._screen_field_mapper.get_walls()):
            self._controller.player_game_group(self._screen_field_mapper.get_pacman(), self._screen_field_mapper.get_container())

        self._controller.ghosts_player(self._screen_field_mapper.get_pacman(), self._screen_field_mapper.get_ghosts())
        self._controller.stupid_ghosts(self._screen_field_mapper.get_ghosts(), self._screen_field_mapper.get_walls())
        self._controller.smart_ghosts(self._screen_field_mapper.get_pacman(),
                                      self._screen_field_mapper.get_ghosts(),
                                      self._screen_field_mapper.get_walls())

    def run(self):
        active = True
        while active:
            if consts.LEARNING:
                self._clock.tick(100)
            else:
                self._clock.tick(100)

            # Process events
            active = self._process_events()

            # Clear the screen
            self._drawer.clear()

            # Check input
            # Move objects ...
            if self._mode == Mode.AUTO:
                self._controller.auto_game()
            else:
                self._player_game()

            self._check_statuses()

            paused = self._check_gameover()

            if not paused:
                # Draw objects ...
                self._drawer.draw()

            # Update the screen
            self._drawer.update()

        pygame.quit()
