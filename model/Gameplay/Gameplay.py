from model.Objects.Interactable.Interactable import Interactable
from model.Objects.background.Wall import Wall


class Collider:
    def _has_collisions(self, character, obstacles):
        for obstacle in obstacles:
            if issubclass(type(obstacle), Interactable):
                if character.collidepoint(obstacle):
                    return obstacle
            else:
                if character.collide(obstacle):
                    return obstacle
        return None

    def check_player_collisions(self, character, obstacles):
        return self._has_collisions(character, obstacles)

    def check_ghost_collisions(self, ghost, obstacles):
        collision = self._has_collisions(ghost, obstacles)
        if collision is None:
            return False
        elif type(collision) is Wall:
            return True
        return False
