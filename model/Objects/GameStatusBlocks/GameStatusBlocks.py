import pygame

from enums import HealthStatus
from model.Dependencies.Dependencies import Dependencies
from model.Screen.CustomScreen import ScreenObject
from model.utils.Utils import ImageUtils


class GameStatusBlock(ScreenObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self._status = None

    def change_status(self):
        raise NotImplementedError

    def current_status(self):
        return self._status


class ImageStatusBlock(GameStatusBlock):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def _read_images(self, img, img_pos):
        return ImageUtils.resize_images(
            ImageUtils.crop_image(
                base_img=Dependencies.load_img(img),
                img_pos=img_pos
            ),
            target_width=self.get_width(),
            target_height=self.get_height()
        )


class StatusText(GameStatusBlock):
    def __init__(self, x, y, width, height, text):
        super().__init__(x, y, width, height)
        text_font = pygame.font.SysFont('Comic Sans MS', 20)
        self._status = text_font.render(text, False, (255, 255, 255))


class HealthStatusBlock(ImageStatusBlock):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self._heart_img = None
        self._empty_heart_img = None

    def init_health_image(self, heart_img, heart_pos, empty_heart_img, empty_heart_pos):
        self._heart_img = self._read_images(img=heart_img, img_pos=heart_pos)[0]
        self._empty_heart_img = self._read_images(img=empty_heart_img, img_pos=empty_heart_pos)[0]

        self._status = self._heart_img

    def get_heart(self):
        return self._heart_img

    def get_empty_heart(self):
        return self._empty_heart_img

    def change_status(self):
        self._status = self.get_empty_heart()


class ScoreStatusTextBlock(GameStatusBlock):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        text_font = pygame.font.SysFont('Comic Sans MS', 30)
        self._status = text_font.render('0000', False, (255, 255, 255))

    def update_score(self, score):
        text_font = pygame.font.SysFont('Comic Sans MS', 30)
        self._status = text_font.render(str(score).rjust(4, '0'), False, (255, 255, 255))


class StatusBlock(ImageStatusBlock):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def init_image(self, img, img_pos):
        self._status = self._read_images(img, img_pos)[0]


class ScoreStatusBlock(StatusBlock):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self._nothing_img = None


class BonusStatusBlock(StatusBlock):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self._image = None

    def init_nothing_img(self, img, img_pos):
        self._nothing_img = self._read_images(img, img_pos)[0]
        self._image = self._status
        self._status = self._nothing_img

    def update_bonus(self):
        self._status = self._image
