import pygame
import sys
from view.Color import Color
from .Sprite import Pacman, Ghost
from enums import Mode
from consts import *


class Game:
    def __init__(self, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, mode=Mode.PLAY):
        pygame.init()
        self.mode = mode
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self._init_sprites()

    def _init_sprites(self):
        self._pacman = Pacman()
        self.ghosts = ...  # TODO

    def _auto_game(self):
        ...  # TODO

    def _player_game(self):
        keyinput = pygame.key.get_pressed()

        if keyinput[pygame.K_LEFT]:
            self._pacman.move(dx=DEFAULT_DX)
        elif keyinput[pygame.K_RIGHT]:
            self._pacman.move(dx=-DEFAULT_DX)
        elif keyinput[pygame.K_UP]:
            self._pacman.move(dx=-DEFAULT_DY)
        elif keyinput[pygame.K_DOWN]:
            self._pacman.move(dx=DEFAULT_DY)

    def run(self):
        pygame.display.set_caption("Pacman")


        while True:
            self.clock.tick(50)

            # Process events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Clear the screen
            self.screen.fill(Color.BLACK)

            # Check input
            # Move objects ...
            if self.mode == Mode.AUTO:
                self._auto_game()
            else:
                self._player_game()

            # Draw objects ...


            # Update the screen
            pygame.display.flip()
