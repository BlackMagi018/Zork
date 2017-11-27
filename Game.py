from Player import Player
from Neighborhood import Neighborhood


class Game:

    def __init__(self):
        self.player = Player()
        self.Map = Neighborhood()
        self.player.location = self.Map.grid.__getitem__(0)
        self.GameOver = False


if __name__ == '__main__':
    Game = Game()
    print("Done")
