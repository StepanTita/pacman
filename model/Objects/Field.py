from enums import PseudoField, GhostsTypes
from model.Objects.Sprites.Sprite import FastGhost, MutantGhost


class Field:
    def __init__(self, pacman_generator, ghosts_generator, walls_generator, coins_generator, points_generator):
        self._pacman_generator = pacman_generator
        self._ghosts_generator = ghosts_generator
        self._walls_generator = walls_generator
        self._coins_generator = coins_generator
        self._points_generator = points_generator

    def get_container(self):
        return self.get_coins(), self.get_points()

    def get_pacman(self):
        return self._pacman_generator.get_field_object()

    def get_ghosts(self):
        return self._ghosts_generator.get_field_objects()

    def get_walls(self):
        return self._walls_generator.get_field_objects()

    def get_coins(self):
        return self._coins_generator.get_field_objects()

    def get_points(self):
        return self._points_generator.get_field_objects()

    def set_instructions(self, named_instructions):
        for ghost in self.get_ghosts():
            if type(ghost) is FastGhost:
                ghost.set_instructions(named_instructions['fast_ghost'])
            elif type(ghost) is MutantGhost:
                ghost.set_instructions(named_instructions['mutant_ghost'])

    def fill(self, cols_count, rows_count, pseudo_field):

        self.cols_count = cols_count
        self.rows_count = rows_count
        self._field = [[None for i in range(self.cols_count)] for j in range(self.rows_count)]

        for i in range(rows_count):
            for j in range(cols_count):
                if pseudo_field[i][j] == PseudoField.WALL.value:
                    self._field[i][j] = self._walls_generator.create(i, j)
                elif pseudo_field[i][j] == PseudoField.COIN.value:
                    self._field[i][j] = self._coins_generator.create(i, j)
                elif pseudo_field[i][j] == PseudoField.POINT.value:
                    self._field[i][j] = self._points_generator.create(i, j)
                elif pseudo_field[i][j] == PseudoField.PACMAN.value:
                    self._field[i][j] = self._pacman_generator.create(i, j)
                elif pseudo_field[i][j] == PseudoField.GHOST.value:
                    self._field[i][j] = self._ghosts_generator.create(i, j)
                elif pseudo_field[i][j] == PseudoField.FAST_GHOST.value:
                    self._ghosts_generator.set_type(GhostsTypes.FAST.value)
                    self._field[i][j] = self._ghosts_generator.create(i, j)
                elif pseudo_field[i][j] == PseudoField.SLOW_GHOST.value:
                    self._ghosts_generator.set_type(GhostsTypes.SLOW.value)
                    self._field[i][j] = self._ghosts_generator.create(i, j)
                elif pseudo_field[i][j] == PseudoField.SLEEPING_GHOST.value:
                    self._ghosts_generator.set_type(GhostsTypes.SLEEPING.value)
                    self._field[i][j] = self._ghosts_generator.create(i, j)
                elif pseudo_field[i][j] == PseudoField.MUTANT_GHOST.value:
                    self._ghosts_generator.set_type(GhostsTypes.MUTANT.value)
                    self._field[i][j] = self._ghosts_generator.create(i, j)

        self._pacman_generator.generate(self)
        self._walls_generator.generate(self)
        self._coins_generator.generate(self)
        self._points_generator.generate(self)
        self._ghosts_generator.generate(self)

    def __getitem__(self, i):
        return self._field[i]
