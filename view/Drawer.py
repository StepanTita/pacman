from model.Objects.Sprites.Sprite import MutantGhost
from .Color import Color
import pygame

'''
# Using Pattern "Mediator"
'''


class Drawer:

    def __init__(self, screen, sprite_drawer, container_drawer, ghost_drawer, wall_drawer, gamestatus_drawer):
        pygame.display.set_caption("Pacman")
        self._screen = screen
        self._sprite_drawer = sprite_drawer
        self._container_drawer = container_drawer
        self._ghost_drawer = ghost_drawer
        self._wall_drawer = wall_drawer
        self.gamestatus_drawer = gamestatus_drawer

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

    def _draw_gamestatus(self):
        self.gamestatus_drawer.draw(self._screen)

    def draw(self):
        self._draw_container()
        self._draw_sprites()
        self._draw_ghosts()
        self._draw_walls()
        self._draw_gamestatus()

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


class GameStatusDrawer:
    def __init__(self, gamestatus):
        self._gamestatus = gamestatus

    def _draw_blocks(self, screen, blocks):
        for block in blocks:
            screen.blit(block.current_status(), block.get_rect())

    def draw(self, screen):
        health_blocks = self._gamestatus.get_current_health()
        self._draw_blocks(screen, health_blocks)

        score_blocks = self._gamestatus.get_current_score()
        self._draw_blocks(screen, score_blocks)
        #
        # bonus_blocks = self._gamestatus.get_bonuses()
        # self._draw_blocks(screen, bonus_blocks)