import pygame


class Utils:
    @staticmethod
    def crop_image(base_img, x1=0, y1=0, x2=0, y2=0, w=128, h=128):
        surfaces = [pygame.Surface((w, h)) for i in range((x2 - x1) * (y2 - y1))]

        range_x = list(range(x1, x2))
        range_y = list(range(y1, y2))

        while len(surfaces) > len(range_x):
            range_x.append(range_x[-1])
        while len(surfaces) > len(range_y):
            range_y.append(range_y[-1])

        for i, j, surf in zip(range_x, range_y, surfaces):
            surf.blit(base_img, (0, 0), (x1 + w * i, y1 + h * j, w, h))
        return surfaces

    @staticmethod
    def rotate_images(images, angle):
        return [pygame.transform.rotate(img, angle) for img in images]

    @staticmethod
    def resize_images(images, target_width, target_height):
        return [pygame.transform.scale(img, (target_width, target_height)) for img in images]
