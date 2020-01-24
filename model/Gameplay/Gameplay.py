from enums import PseudoField
from model.Objects.Interactable.Interactable import Coin, Point, Interactable
from model.Objects.Sprites.Sprite import Ghost
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
        collision = self._has_collisions(character, obstacles)
        if collision is None:
            return None
        elif type(collision) is Wall:
            return Wall
        elif type(collision) is Coin:
            obstacles.remove(collision)
            return Coin
        elif type(collision) is Point:
            obstacles.remove(collision)
            return Point
        elif issubclass(type(collision), Ghost):
            return Ghost
        return False

    def check_ghost_collisions(self, ghost, obstacles):
        collision = self._has_collisions(ghost, obstacles)
        if collision is None:
            return False
        elif type(collision) is Wall:
            return True
        return False
