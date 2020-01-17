from model.Events.MoveEvent import PacmanMoveEvent
from model.Game import Game
import consts

if __name__ == '__main__':
    # Custom Events
    PacmanMoveEvent.create_event(consts.MOUTH_SPEED)

    # Game init
    game = Game()
    game.run()