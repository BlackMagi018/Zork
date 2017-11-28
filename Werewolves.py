from random import randint
from Monster import Monster
from SourStraws import SourStraws
from Weapon import Weapon
from ChocolateBar import ChocolateBar


class Werewolves(Monster):

    def __init__(self):
        self.name = "Werewolf"
        super().__init__(self.name, 200, randint(0, 40))

    def damage(self, weapon: Weapon, atk: int):
        if weapon.name == "Chocolate Bar" or weapon.name == "Sour Straws":
            self.health -= 0
        else:
            self.health -= atk * weapon.mod
            if self.health <= 0:
                self.home.resurrect(self)
