from collections import namedtuple


# Utils
ImagePosition = namedtuple('ImagePosition', ['x1', 'y1', 'x2', 'y2'])

# --------- Game -------------
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
PACMAN = 'assets/imgs/sprites.png'
WALLS = 'assets/imgs/walls.png'
# --------- Sprites ------------
DEFAULT_DX = 5
DEFAULT_DY = 5
BLOCK_WIDTH = 60
BLOCK_HEIGHT = 60
DEFAULT_X = 0
DEFAULT_Y = 0
PACMAN_SPEED = 5
PACMAN_STATES = 4
MOUTH_SPEED = 110
BASE_SPRITE_POS = ImagePosition(x1=0, x2=4, y1=0, y2=1)
# --------- Physics ------------

# --------- Walls ------------
BASE_WALL_POS = ImagePosition(x1=3, x2=4, y1=5, y2=6)