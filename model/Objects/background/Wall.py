import pygame

from model.dependencies.Dependencies import Dependencies
from model.utils.Utils import Utils


class Wall:
    def __init__(self, img, img_pos, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

        self.image = Utils.resize_images(
            Utils.crop_image(
                base_img=Dependencies.load_img(img),
                x1=img_pos.x1, x2=img_pos.x2,
                y1=img_pos.y1, y2=img_pos.y2
            ), target_width=width, target_height=height
        )

    def current_state(self):
        return self.image


class WallGenerator:

    def __init__(self, wall_img, img_pos,
                 screen_width, screen_height,
                 block_width, block_height):
        self.base_wall_img = wall_img
        self.base_wall_img_pos = img_pos
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.block_width = block_width
        self.block_height = block_height

    def generate_walls(self, x1, y1, x2, y2, field):
        for i in range(x1, x2):
            for j in range(y1, y2):
                field[i][j] = Wall(img=self.base_wall_img, img_pos=self.base_wall_img_pos,
                                   x=i * self.screen_width, y=j * self.screen_height,
                                   width=self.screen_width, height=self.block_height)

    def generate_frame(self, field):
        self.generate_walls(0, self.screen_width // self.block_width,
                            0, self.screen_height // self.screen_height, field)
