from random import randint
from Monster import Monster
from SourStraws import SourStraws
from Weapon import Weapon
from ChocolateBar import ChocolateBar


class Werewolves(Monster):

    def __init__(self):
        super().__init__(200, randint(0, 40))

    def damage(self, weapon, atk):
        assert isinstance(Weapon, weapon)
        assert isinstance(int, atk)
        if isinstance(ChocolateBar, weapon) | isinstance(SourStraws, weapon):
            self.health -= 0
        else:
            self.health -= atk * weapon.mod
            if self.health <= 0:
                self.home.resurrect(self)
