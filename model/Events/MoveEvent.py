import pygame


class MoveEvent:
    __instance = None

    def __init__(self, identifier, delay):
        MoveEvent.__instance = self
        self.identifier = identifier
        self.delay = delay
        pygame.time.set_timer(identifier, delay)


class PacmanMoveEvent(MoveEvent):
    __instance = None

    def __init__(self, identifier, delay):
        PacmanMoveEvent.__instance = self
        super().__init__(identifier, delay)

    @staticmethod
    def create_event(delay, identifier=pygame.USEREVENT+1):
        return PacmanMoveEvent.__instance if PacmanMoveEvent.__instance else PacmanMoveEvent(identifier, delay)

    @staticmethod
    def get_event_id():
        return -1 if PacmanMoveEvent.__instance is None else PacmanMoveEvent.__instance.identifier


class CoinTossEvent(MoveEvent):
    __instance = None

    def __init__(self, identifier, delay):
        CoinTossEvent.__instance = self
        super().__init__(identifier, delay)

    @staticmethod
    def create_event(delay, identifier=pygame.USEREVENT + 2):
        return CoinTossEvent.__instance if CoinTossEvent.__instance else CoinTossEvent(identifier, delay)

    @staticmethod
    def get_event_id():
        return -1 if CoinTossEvent.__instance is None else CoinTossEvent.__instance.identifier