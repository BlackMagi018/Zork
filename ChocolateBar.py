from random import uniform
from Weapon import Weapon


class ChocolateBar(Weapon):

    def __init__(self):
        text = "Chocolate Bar"
        mod = uniform(2, 2.4)
        ammo = 4
        super().__init__(text, mod, ammo)
