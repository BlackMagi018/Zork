from random import uniform
from Weapon import Weapon


class SourStraws(Weapon):
    def __init__(self):
        self.name = "Sour Straws"
        self.mod = round(uniform(1, 1.75),2)
        self.ammo = 2
        super().__init__(self.name, self.mod, self.ammo)
