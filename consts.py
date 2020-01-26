from collections import namedtuple

# ImageUtils
ImagePosition = namedtuple('ImagePosition', ['x1', 'y1', 'x2', 'y2', 'w', 'h'])

LEARNING = False
if LEARNING:
    BLOCK_SIZE = 60
    BLOCK_WIDTH = BLOCK_SIZE
    BLOCK_HEIGHT = BLOCK_SIZE
    PACMAN_WIDTH = BLOCK_WIDTH
    PACMAN_HEIGHT = BLOCK_HEIGHT
    WALL_WIDTH = BLOCK_WIDTH
    WALL_HEIGHT = BLOCK_HEIGHT
    COIN_WIDTH = BLOCK_WIDTH
    COIN_HEIGHT = BLOCK_HEIGHT
    GHOST_WIDTH = PACMAN_WIDTH
    GHOST_HEIGHT = PACMAN_HEIGHT
    # --------- SPEED ------------
    PACMAN_SPEED = BLOCK_SIZE // 20
    GHOSTS_SPEED = PACMAN_SPEED // 2
else:
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
    GHOST_WIDTH = PACMAN_WIDTH
    GHOST_HEIGHT = PACMAN_HEIGHT
    POINT_WIDTH = BLOCK_WIDTH
    POINT_HEIGHT = BLOCK_HEIGHT
    # --------- SPEED ------------
    PACMAN_SPEED = BLOCK_SIZE // 20
    GHOSTS_SPEED = PACMAN_SPEED // 2

# --------- PATHS -------------
FIELD_NAME = 'maps/map_2.txt'
PACMAN = 'assets/imgs/sprites.png'
WALLS = 'assets/imgs/walls.png'
COINS = 'assets/imgs/coin.png'
POINTS = 'assets/imgs/sprites.png'
GHOSTS = 'assets/imgs/sprites.png'
HEART = 'assets/imgs/heart.png'
EHEART = 'assets/imgs/heart2.png'
CROSS = 'assets/imgs/cross.png'
RASP = 'assets/imgs/sprites.png'
LEMON = 'assets/imgs/sprites.png'
STRAW = 'assets/imgs/sprites.png'
PEAR = 'assets/imgs/sprites.png'
# --------- Objects ------------
BASE_SPRITE_POS = ImagePosition(x1=0, x2=4, y1=0, y2=1, w=128, h=128)
ALL_SPRITE_POS = ImagePosition(x1=0, x2=4, y1=0, y2=4, w=128, h=128)
BASE_WALL_POS = ImagePosition(x1=5, x2=6, y1=3, y2=4, w=63, h=63)

BASE_COIN_POS = ImagePosition(x1=0, x2=5, y1=0, y2=1, w=200, h=250)
BASE_GHOST_POS = ImagePosition(x1=0, x2=8, y1=4, y2=8, w=128, h=128)
BASE_INV_POS = ImagePosition(x1=4, x2=6, y1=3, y2=4, w=128, h=128)
BASE_POINT_POS = ImagePosition(x1=5, x2=6, y1=0, y2=1, w=128, h=128)

BASE_RASP_POS = ImagePosition(x1=4, x2=5, y1=1, y2=2, w=128, h=128)
BASE_LEMON_POS = ImagePosition(x1=5, x2=6, y1=1, y2=2, w=128, h=128)
BASE_STRAW_POS = ImagePosition(x1=6, x2=7, y1=1, y2=2, w=128, h=128)
BASE_PEAR_POS = ImagePosition(x1=7, x2=8, y1=1, y2=2, w=128, h=128)

BASE_HEART_POS = ImagePosition(x1=0, x2=1, y1=0, y2=1, w=200, h=190)
BASE_EHEART_POS = ImagePosition(x1=0, x2=1, y1=0, y2=1, w=200, h=190)
BASE_CROSS_POS = ImagePosition(x1=0, x2=1, y1=0, y2=1, w=240, h=240)
# --------- DIFFERENT ------------
GHOSTS_STATES = 8
HEALTH = 3
INVINSIBILITY_TIME = 2000
SPEED_TIME = 5000
BREAKER_TIME = 2000
COIN_SCORE = 5
POINT_SCORE = 1
# --------- INSTRUCTIONS ------------
FAST_INSTRUCTIONS = 'Instructions/fast_instructions.txt'
MUTANT_INSTRUCTIONS = 'Instructions/mutant_instructions.txt'
# --------- ANIMATIONS ------------
MOUTH_SPEED = 110
COIN_SPEED = 100
GHOST_ANIM_SPEED = 125
