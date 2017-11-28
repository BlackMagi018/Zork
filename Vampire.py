from random import randint

from ChocolateBar import ChocolateBar
from Monster import Monster
from Weapon import Weapon


class Vampire(Monster):

    def __init__(self):
        self.name = "Vampire"
        super().__init__(self.name, randint(100, 200), randint(10, 20))

    def damage(self, weapon: Weapon, atk: int):
        if weapon.name == "Chocolate Bar":
            self.health += 0
        else:
            self.health -= atk * weapon.mod
            if self.health <= 0:
                self.home.resurrect(self)
