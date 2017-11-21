from random import randint
from HersheyKiss import HersheyKiss
from SourStraws import SourStraws
from ChocolateBar import ChocolateBar
from NerdBombs import NerdBombs


class Player:
    health = randint(100, 125)
    attack = randint(10, 20)
    arsenal = []

    def __init__(self):
        x = HersheyKiss
        self.arsenal.append(x)
        for i in range(0, 9):
            c = randint(0, 2)
            if c == 0:
                x = SourStraws
            elif c == 1:
                x = ChocolateBar
            else:
                x = NerdBombs
            self.arsenal.append(x)
