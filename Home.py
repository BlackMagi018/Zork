from Monster import Monster  # code uses Monster.Monster
from Person import Person  # code uses Person.Person
from Weapon import Weapon  # code uses Weapon.Weapon
from Player import Player  # code uses Player.Player


class Home:
    """A seemingly normal house is hiding pure horror waiting to attack"""

    def __init__(self):
        """Constructor for Home class

        Attributes:
            Thrall - list of monsters inside home
            Left - reference to home to the left of the home
            Right - reference to home to the right of the home
            Population - count of monsters minus any of the Person class
            Grid - reference to the Neighborhoods object that contains this home
        """

        self.thrall = []
        self.left = None
        self.right = None
        self.population = 0
        self.grid = None

    def damage(self, weapon: Weapon, attack: int):
        """Deal damage to each monster in home

            Parameters:
            weapon - Weapon uses to attack monster
            atk - player's attack power
        """

        for monsters in self.thrall:
            monsters.damage(weapon, attack)

    def revenge(self, player: Player):
        """Deal damage to player from each monster

            Parameters:
            player - Player object
        """

        for monsters in self.thrall:
            player.health -= monsters.attack

    def resurrect(self, monster: Monster):
        """Replace a defeated monster with a Person object

            Parameters:
            monster - Monster object
        """

        mid = self.thrall.index(monster)
        person = Person()
        self.thrall.__setitem__(mid, person)
        self.population -= 1
        self.grid.totalMonsters -= 1
