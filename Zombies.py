from random import randint
from Monster import Monster
from SourStraws import SourStraws
from Weapon import Weapon


class Zombies(Monster):

    def __init__(self):
        self.name = "Zombie"
        super().__init__(self.name, randint(50, 100), randint(0, 10))

    def damage(self, weapon: Weapon, atk: int):
        if weapon.name == "Sour Straws":
            self.health -= atk * 5
            if self.health <= 0:
                self.home.resurrect(self)
        else:
            self.health -= atk * weapon.mod
            if self.health <= 0:
                self.home.resurrect(self)
