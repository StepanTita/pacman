from model.Objects.Interactable.Interactable import Coin
from model.Objects.background.Wall import Wall


class Collider:
    def _has_collisions(self, character, obstacles):
        for obstacle in obstacles:
            if character.collide(obstacle):
                return obstacle
        return None

    def check_collisions(self, character, obstacles):
        collision = self._has_collisions(character, obstacles)
        if collision is None:
            return False
        if type(collision) is Wall:
            return True
        if type(collision) is Coin:
            obstacles.remove(collision)
            return False

        return False
