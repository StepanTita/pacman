from enums import PseudoField


class Field:
    def __init__(self, pacman_generator, ghosts_generator, walls_generator, coins_generator):
        self._pacman_generator = pacman_generator
        self._ghosts_generator = ghosts_generator
        self._walls_generator = walls_generator
        self._coins_generator = coins_generator

    def get_container(self):
        return self.get_walls(), self.get_coins()

    def get_pacman(self):
        return self._pacman_generator.get_field_object()

    def get_ghosts(self):
        return self._ghosts_generator.get_field_objects()

    def get_walls(self):
        return self._walls_generator.get_field_objects()

    def get_coins(self):
        return self._coins_generator.get_field_objects()

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
                elif pseudo_field[i][j] == PseudoField.PACMAN.value:
                    self._field[i][j] = self._pacman_generator.create(i, j)
                # elif pseudo_field[i][j] == PseudoField.GHOST.value:
                #     self._field[i][j] = self._ghosts_generator.create(i, j)

        self._pacman_generator.generate(self)
        self._walls_generator.generate(self)
        self._coins_generator.generate(self)
        # self._ghosts_generator.generate(self)

    def __getitem__(self, i):
        return self._field[i]
