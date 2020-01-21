class ScreenFieldMapper:

    def __init__(self, screen, field):
        self._screen = screen
        self._field = field

    def get_screen(self):
        return self._screen

    def get_field(self):
        return self._field

    def get_pacman(self):
        return self._field.get_pacman()

    def get_ghosts(self):
        return self._field.get_ghosts()

    def get_walls(self):
        return self._field.get_walls()

    def get_screen_width(self):
        return self._screen.get_width()

    def get_screen_height(self):
        return self._screen.get_height()

    def left_screen_border(self):
        return 0

    def right_screen_border(self):
        return self.get_screen_width()

    def up_screen_border(self):
        return 0

    def down_screen_border(self):
        return self.get_screen_height()

    def change_coins_state(self):
        for sprite in self._field.get_coins().sprites():
            sprite.next_state()
        return self._field.get_coins()