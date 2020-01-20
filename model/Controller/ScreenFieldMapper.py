class ScreenFieldMapper:

    def __init__(self, screen, field):
        self._screen = screen
        self._field = field

    def get_screen(self):
        return self._screen

    def get_field(self):
        return self._field

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
