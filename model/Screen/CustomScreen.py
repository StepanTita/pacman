import pygame


class CustomScreen:
    def __init__(self, screen, status_height):
        self._screen = screen
        self._status_height = status_height

    def get_width(self):
        return self._screen.get_width()

    def get_height(self):
        return self._screen.get_height() - self._status_height

    def fill(self, *args, **kwargs):
        self._screen.fill(*args, **kwargs)

    def blit(self, *args, **kwargs):
        self._screen.blit(*args, **kwargs)


class ScreenObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self._rect = pygame.Rect(x, y, width, height)

    def get_rect(self):
        return self._rect

    def get_width(self):
        return self._rect.width

    def get_height(self):
        return self._rect.height

    def x(self):
        return self._rect.x

    def y(self):
        return self._rect.y