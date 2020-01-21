from collections import namedtuple


# ImageUtils
ImagePosition = namedtuple('ImagePosition', ['x1', 'y1', 'x2', 'y2', 'w', 'h'])
# --------- Sprites ------------
BLOCK_SIZE = 60
BLOCK_WIDTH = BLOCK_SIZE
BLOCK_HEIGHT = BLOCK_SIZE
PACMAN_SPEED = BLOCK_SIZE // 12
PACMAN_STATES = 4
MOUTH_SPEED = 110
BASE_SPRITE_POS = ImagePosition(x1=0, x2=4, y1=0, y2=1, w=128, h=128)
# --------- Game -------------
FIELD_NAME = 'maps/basic_map.txt'
SCREEN_WIDTH = BLOCK_SIZE * 12
SCREEN_HEIGHT = BLOCK_SIZE * 8
PACMAN = 'assets/imgs/sprites.png'
WALLS = 'assets/imgs/walls.png'
# --------- Walls ------------
BASE_WALL_POS = ImagePosition(x1=5, x2=6, y1=3, y2=4, w=63, h=63)