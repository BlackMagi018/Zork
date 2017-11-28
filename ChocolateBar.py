from random import uniform
from Weapon import Weapon


class ChocolateBar(Weapon):

    def __init__(self):
        self.text = "Chocolate Bar"
        self.mod = round(uniform(2, 2.4),2)
        self.ammo = 4
        super().__init__(self.text, self.mod, self.ammo)
