from enums import PseudoField


class Field:
    def __init__(self, pacman, ghosts, walls_generator):
        self.pacman = pacman
        self.ghosts = ghosts
        self.walls_generator = walls_generator

    def get_pacman(self):
        return self.pacman

    def get_ghosts(self):
        return self.ghosts

    def get_walls(self):
        return self.walls_generator.get_walls()

    def fill(self, cols_count, rows_count, pseudo_field):

        self.cols_count = cols_count
        self.rows_count = rows_count
        self._field = [[None for i in range(self.cols_count)] for j in range(self.rows_count)]

        for i in range(rows_count):
            for j in range(cols_count):
                if pseudo_field[i][j] == PseudoField.WALL.value:
                    self._field[i][j] = self.walls_generator.create_wall(i, j)

        self.walls_generator.generate_walls(self)

    def __getitem__(self, i):
        return self._field[i]
