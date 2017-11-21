from random import uniform
from Weapon import Weapon


class NerdBombs(Weapon):

    def __init__(self):
        text = "Nerd Bombs"
        mod = uniform(3.5, 5)
        ammo = 1
        super().__init__(text, mod, ammo)
