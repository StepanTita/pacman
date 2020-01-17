import pygame
import os


class Dependencies:

    @staticmethod
    def load_img(path):
        return pygame.image.load(os.path.join(os.getcwd(), path)).convert_alpha()


