from Monster import Monster
from Persons import Persons
from Weapon import Weapon
from Player import Player


class Home:
    """A seemingly normal house is hiding pure horror waiting to attack"""

    def __init__(self):
        self.thrall = []
        self.left = None
        self.right = None
        self.population = 0
        self.grid = None

    def damage(self, weapon: Weapon, attack: int):
        for monsters in self.thrall:
            monsters.damage(weapon, attack)

    def revenge(self, player: Player):
        for monsters in self.thrall:
            player.health -= monsters.attack

    def resurrect(self, monster: Monster):
        mid = self.thrall.index(monster)
        person = Persons()
        self.thrall.__setitem__(mid, person)
        self.population -= 1
        self.grid.totalMonsters -= 1
