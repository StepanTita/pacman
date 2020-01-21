import pygame


class ImageUtils:
    @staticmethod
    def crop_image(base_img, img_pos):
        surfaces = [pygame.Surface((img_pos.w, img_pos.h), pygame.SRCALPHA)
                    for i in range((img_pos.x2 - img_pos.x1) * (img_pos.y2 - img_pos.y1))]

        range_x = list(range(img_pos.x1, img_pos.x2))
        range_y = list(range(img_pos.y1, img_pos.y2))

        while len(surfaces) > len(range_x):
            range_x.append(range_x[-1])
        while len(surfaces) > len(range_y):
            range_y.append(range_y[-1])

        for i, j, surf in zip(range_x, range_y, surfaces):
            surf.blit(base_img, (0, 0), (img_pos.x1 + img_pos.w * i, img_pos.y1 + img_pos.h * j, img_pos.w, img_pos.h))
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