import pygame

from model.Events.MoveEvent import PacmanMoveEvent
from model.utils.Cropper import Cropper
from model.Objects.Sprites.Sprite import Pacman
from enums import Mode, Direction
import consts
from view.Drawer import Drawer, SpriteDrawer, WallDrawer


class Game:
    def __init__(self, screen_width=consts.SCREEN_WIDTH, screen_height=consts.SCREEN_HEIGHT,
                 block_width=consts.BLOCK_WIDTH, block_height=consts.BLOCK_HEIGHT, mode=Mode.PLAY):
        pygame.init()
        screen = pygame.display.set_mode((screen_width, screen_height))

        self.block_width = block_width
        self.block_height = block_height

        self._field = [
            [None for _ in range(screen_width // block_width)] for _ in range(screen_height // block_height)
        ]

        self._init_sprites()
        self._init_walls()

        self.mode = mode

        self._drawer = Drawer(
            screen=screen,
            sprite_drawer=SpriteDrawer(self._pacman),
            wall_drawer=WallDrawer(self.walls)
        )
        self._clock = pygame.time.Clock()

    def _init_walls(self):
        self.walls = []

    def _init_sprites(self):
        self._pacman = Pacman(img=consts.PACMAN, speed=consts.SPEED, img_pos=Cropper(x1=0, x2=consts.SPRITE_STATES,
                                                                                     y1=0, y2=1),
                              x=consts.BLOCK_WIDTH, y=consts.BLOCK_HEIGHT,
                              width=self.block_width, height=self.block_height)
        self._ghosts = ...  # TODO

    def _auto_game(self):
        ...  # TODO

    def _player_game(self):
        keyinput = pygame.key.get_pressed()

        if keyinput[pygame.K_LEFT] and self._pacman.rect.x > 0:
            if self._pacman.moving_direction != Direction.RIGHT:
                self._pacman.update_direction(Direction.RIGHT)
            self._pacman.move(dx=-self._pacman.speed)
        elif keyinput[pygame.K_RIGHT] and self._pacman.rect.x < consts.SCREEN_WIDTH - self._pacman.rect.width:
            if self._pacman.moving_direction != Direction.LEFT:
                self._pacman.update_direction(Direction.LEFT)
            self._pacman.move(dx=self._pacman.speed)
        elif keyinput[pygame.K_UP] and self._pacman.rect.y > 0:
            if self._pacman.moving_direction != Direction.UP:
                self._pacman.update_direction(Direction.UP)
            self._pacman.move(dy=-self._pacman.speed)
        elif keyinput[pygame.K_DOWN] and self._pacman.rect.y < consts.SCREEN_HEIGHT - self._pacman.rect.height:
            if self._pacman.moving_direction != Direction.BOT:
                self._pacman.update_direction(Direction.BOT)
            self._pacman.move(dy=self._pacman.speed)

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
            if self.mode == Mode.AUTO:
                self._auto_game()
            else:
                self._player_game()

            # Draw objects ...
            self._drawer.draw()

            # Update the screen
            self._drawer.update()

        pygame.quit()
