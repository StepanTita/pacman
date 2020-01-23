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
GHOST_WIDTH = PACMAN_WIDTH
GHOST_HEIGHT = PACMAN_HEIGHT
# --------- PATHS -------------
FIELD_NAME = 'maps/basic_map.txt'
PACMAN = 'assets/imgs/sprites.png'
WALLS = 'assets/imgs/walls.png'
COINS = 'assets/imgs/coin.png'
GHOSTS = 'assets/imgs/sprites.png'
# --------- Objects ------------
BASE_SPRITE_POS = ImagePosition(x1=0, x2=4, y1=0, y2=1, w=128, h=128)
BASE_WALL_POS = ImagePosition(x1=5, x2=6, y1=3, y2=4, w=63, h=63)
BASE_COIN_POS = ImagePosition(x1=0, x2=5, y1=0, y2=1, w=200, h=250)
BASE_GHOST_POS = ImagePosition(x1=0, x2=8, y1=4, y2=8, w=128, h=128)
# --------- SPEED ------------
PACMAN_SPEED = BLOCK_SIZE // 20
GHOSTS_SPEED = PACMAN_SPEED // 2
MOUTH_SPEED = 110
COIN_SPEED = 100
GHOST_ANIM_SPEED = 125
# --------- DIFFERENT ------------
GHOSTS_STATES = 8
# --------- INSTRUCTIONS ------------
FAST_INSTRUCTIONS = 'Instructions/fast_instructions.txt'
MUTANT_INSTRUCTIONS = 'Instructions/mutant_instructions.txt'
