from Player import Player
from Neighborhood import Neighborhood


class Game:

    def __init__(self):
        self.player = Player()
        self.Map = Neighborhood()


if __name__ == '__main__':
    Game = Game()
