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

    def get_coins(self):
        return self._field.get_coins()

    def get_points(self):
        return self._field.get_points()

    def get_straw(self):
        return self._field.get_straw()

    def get_lemon(self):
        return self._field.get_lemon()

    def get_rasp(self):
        return self._field.get_rasp()

    def get_pear(self):
        return self._field.get_pear()

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

    def _change_sprite_state(self, sprite_type):
        for sprite in sprite_type.sprites():
            sprite.next_state()

    def change_coins_state(self):
        self._change_sprite_state(self.get_coins())

    def change_ghosts_state(self):
        self._change_sprite_state(self.get_ghosts())

    def get_container(self):
        return self._field.get_container()

    def coin_found(self):
        self._field.coin_found()

    def point_found(self):
        self._field.point_found()

    def is_victory(self):
        return self._field.is_victory()