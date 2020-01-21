from collections import namedtuple


# ImageUtils
ImagePosition = namedtuple('ImagePosition', ['x1', 'y1', 'x2', 'y2', 'w', 'h'])
# --------- SIZES ------------
BLOCK_SIZE = 60
BLOCK_WIDTH = BLOCK_SIZE
BLOCK_HEIGHT = BLOCK_SIZE
PACMAN_WIDTH = BLOCK_WIDTH // 2
PACMAN_HEIGHT = BLOCK_HEIGHT // 2
WALL_WIDTH = BLOCK_WIDTH
WALL_HEIGHT = BLOCK_HEIGHT
COIN_WIDTH = BLOCK_WIDTH // 2
COIN_HEIGHT = BLOCK_HEIGHT // 2
SCREEN_WIDTH = BLOCK_SIZE * 12
SCREEN_HEIGHT = BLOCK_SIZE * 8
# --------- PATHS -------------
FIELD_NAME = 'maps/basic_map.txt'
PACMAN = 'assets/imgs/sprites.png'
WALLS = 'assets/imgs/walls.png'
COINS = 'assets/imgs/coin.png'
# --------- Objects ------------
BASE_SPRITE_POS = ImagePosition(x1=0, x2=4, y1=0, y2=1, w=128, h=128)
BASE_WALL_POS = ImagePosition(x1=5, x2=6, y1=3, y2=4, w=63, h=63)
BASE_COIN_POS = ImagePosition(x1=0, x2=5, y1=0, y2=1, w=200, h=250)
# --------- SPEED ------------
PACMAN_SPEED = BLOCK_SIZE // 16
MOUTH_SPEED = 110
COIN_SPEED = 100