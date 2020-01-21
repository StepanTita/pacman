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
