from .Color import Color
import pygame

'''
# Using Pattern "Mediator"
'''


class Drawer:

    def __init__(self, screen, sprite_drawer, wall_drawer):
        pygame.display.set_caption("Pacman")
        self._screen = screen
        self._sprite_drawer = sprite_drawer
        self._wall_drawer = wall_drawer

    def clear(self):
        self._screen.fill(Color.BLACK)

    def _draw_walls(self):
        self._wall_drawer.draw(self._screen)

    def _draw_sprites(self):
        self._sprite_drawer.draw(self._screen)

    def draw(self):
        self._draw_walls()
        self._draw_sprites()

    def update(self):
        pygame.display.update()


class SpriteDrawer:

    def __init__(self, sprite, ghosts):
        self.sprite = sprite

    def draw(self, screen):
        screen.blit(self.sprite.current_state(), self.sprite.get_rect())
        ...


class WallDrawer:

    def __init__(self, walls):
        self._walls = walls

    def draw(self, screen):
        for sprite in self._walls.sprites():
            screen.blit(sprite.current_state(), sprite.get_rect())
