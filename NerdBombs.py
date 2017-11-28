from random import uniform
from Weapon import Weapon


class NerdBombs(Weapon):

    def __init__(self):
        self.text = "Nerd Bombs"
        self.mod = round(uniform(3.5, 5),2)
        self.ammo = 1
        super().__init__(self.text, self.mod, self.ammo)
