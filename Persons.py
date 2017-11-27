from Monster import Monster
from Weapon import Weapon


class Persons(Monster):

    def __init__(self):
        self.name = "Person"
        super().__init__(self.name, 100, -1)

    def damage(self, weapon, atk):
        assert isinstance(Weapon, weapon)
        assert isinstance(int, atk)
        self.health += 0
