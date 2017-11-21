from random import uniform
from Weapon import Weapon


class SourStraws(Weapon):
    def __init__(self):
        name = "Sour Straws"
        mod = uniform(1, 1.75)
        ammo = 2
        super().__init__(name, mod, ammo)
