import pygame

from enums import Direction


class ImageUtils:
    @staticmethod
    def crop_image(base_img, img_pos):
        surfaces = []

        for j in range(img_pos.y1, img_pos.y2):
            for i in range(img_pos.x1, img_pos.x2):
                surf = pygame.Surface((img_pos.w, img_pos.h), pygame.SRCALPHA)
                surf.blit(base_img, (0, 0),
                          (img_pos.x1 + img_pos.w * i, img_pos.y1 + img_pos.h * j, img_pos.w, img_pos.h))
                surfaces.append(surf)
        return surfaces

    @staticmethod
    def rotate_images(images, angle):
        return [pygame.transform.rotate(img, angle) for img in images]

    @staticmethod
    def resize_images(images, target_width, target_height):
        return [pygame.transform.scale(img, (target_width, target_height)) for img in images]


class FileUtils:
    @staticmethod
    def lines_to_field(lines):
        rows, cols = lines[0].split()
        return int(rows), int(cols), [list(line) for line in lines[1:]]


class BaseUtils:
    @staticmethod
    def divide_chunks(lst, n):
        # looping till length lst
        result = []
        for i in range(0, len(lst), n):
            result.append(lst[i:i + n])
        return result

    @staticmethod
    def create_instructions(**kwargs):
        instruction_map = {'<': Direction.LEFT,
                           '>': Direction.RIGHT,
                           '^': Direction.UP,
                           'V': Direction.DOWN}

        result = dict()

        for key, instructions in kwargs.items():
            result[key] = []
            for instruction in instructions:
                direction, times = instruction
                result[key] += [instruction_map[direction]] * int(times)
        return result
