import consts


class GameStatus:
    def __init__(self, max_health, health_blocks, health_text_block,
                 point_score_block, points_score_text_block,
                 coint_score_block, coins_score_text_block,
                 bonuses):
        self._health = max_health
        self._max_health = max_health
        self._points_score = 0
        self._coins_score = 0

        self._bonuses = bonuses

        self._health_text_block = health_text_block
        self._health_blocks = health_blocks

        self._point_score_block = point_score_block
        self._points_score_text_block = points_score_text_block
        self._coint_score_block = coint_score_block
        self._coins_score_text_block = coins_score_text_block

    def change_status(self):
        if self._health > 0:
            self._health -= 1
            self._health_blocks[self._health].change_status()

    def update_points_score(self):
        self._points_score += consts.POINT_SCORE
        self._points_score_text_block.update_score(self._points_score)

    def update_coins_score(self):
        self._coins_score += consts.COIN_SCORE
        self._coins_score_text_block.update_score(self._coins_score)

    def update_bonuses(self, bonus_type):
        self._bonuses[bonus_type].update_bonus()

    def get_current_health(self):
        return [self._health_text_block] + self._health_blocks

    def get_current_score(self):
        return [self._point_score_block, self._points_score_text_block, self._coint_score_block,
                self._coins_score_text_block]

    def get_current_bonuses(self):
        return self._bonuses.values()
