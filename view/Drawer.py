from model.Objects.Sprites.Sprite import MutantGhost
from .Color import Color
import pygame

'''
# Using Pattern "Mediator"
'''


class Drawer:

    def __init__(self, screen, sprite_drawer, container_drawer, ghost_drawer, wall_drawer):
        pygame.display.set_caption("Pacman")
        self._screen = screen
        self._sprite_drawer = sprite_drawer
        self._container_drawer = container_drawer
        self._ghost_drawer = ghost_drawer
        self._wall_drawer = wall_drawer

    def clear(self):
        self._screen.fill(Color.BLACK)

    def _draw_container(self):
        self._container_drawer.draw(self._screen)

    def _draw_sprites(self):
        self._sprite_drawer.draw(self._screen)

    def _draw_ghosts(self):
        self._ghost_drawer.draw(self._screen)

    def _draw_walls(self):
        self._wall_drawer.draw(self._screen)

    def draw(self):
        self._draw_container()
        self._draw_sprites()
        self._draw_ghosts()
        self._draw_walls()

    def update(self):
        pygame.display.update()


class SpriteDrawer:

    def __init__(self, sprite):
        self._sprite = sprite

    def draw(self, screen):
        screen.blit(self._sprite.current_state(), self._sprite.get_rect())


class ContainerDrawer:

    def __init__(self, container):
        self._container = container

    def draw(self, screen):
        for group in self._container:
            for sprite in group.sprites():
                screen.blit(sprite.current_state(), sprite.get_rect())


class GhostDrawer:
    def __init__(self, ghosts):
        self._ghosts = ghosts

    def draw(self, screen):
        for sprite in self._ghosts.sprites():
            screen.blit(sprite.current_state(), sprite.get_rect())


class WallDrawer:
    def __init__(self, walls):
        self._walls = walls

    def draw(self, screen):
        for sprite in self._walls.sprites():
            screen.blit(sprite.current_state(), sprite.get_rect())