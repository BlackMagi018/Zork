from Monster import Monster
from Persons import Persons


class Home:
    """A seemingly normal house is hiding pure horror waiting to attack"""

    def __init__(self):
        self.thrall = []
        self.left = None
        self.right = None

    def damage(self, weapon, player):
        for monsters in self.thrall:
            assert isinstance(monsters, Monster)
            monsters.damage(weapon, player.attack)

    def resurrect(self, monster):
        assert isinstance(Monster,monster)
        mid = self.thrall.index(monster)
        person = Persons
        self.thrall.__setitem__(mid, person)
