from random import randint
from Monster import Monster
from NerdBombs import NerdBombs
from Weapon import Weapon


class Ghouls(Monster):

    def __init__(self):
        super().__init__(randint(40, 80), randint(15, 30))

    def damage(self, weapon, atk):
        assert isinstance(Weapon, weapon)
        assert isinstance(int, atk)
        if isinstance(NerdBombs, weapon):
            self.health -= atk * 5
            if self.health <= 0:
                self.home.resurrect(self)
        else:
            self.health -= atk * weapon.mod
            if self.health <= 0:
                self.home.resurrect(self)
