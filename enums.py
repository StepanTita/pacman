from enum import Enum


class Mode(Enum):
    AUTO = 1
    PLAY = 2


class Direction(Enum):
    LEFT = 90
    RIGHT = -90
    BOT = 180
    UP = 0


class PseudoField(Enum):
    PACMAN = 'P'
    WALL = '#'
    COIN = 'C'
    GHOST = 'G'
    FAST_GHOST = 'F'
    SLOW_GHOST = 'S'
    SLEEPING_GHOST = 'Z'
    MUTANT_GHOST = 'M'


class GhostsTypes(Enum):
    MUTANT = 0
    SLOW = 1
    FAST = 2
    SLEEPING = 3
