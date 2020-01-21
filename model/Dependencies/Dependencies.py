import pygame
import os


class Dependencies:

    @staticmethod
    def load_img(path):
        return pygame.image.load(os.path.join(os.getcwd(), path)).convert_alpha()

    @staticmethod
    def load_file(path):
        lines = []
        with open(path) as file:
            first_row = file.readline()
            rows, cols = map(int, first_row.split())
            lines.append(first_row)
            for i in range(rows):
                lines.append(file.readline())
        return lines
