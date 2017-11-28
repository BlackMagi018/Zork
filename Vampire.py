from random import randint  # code uses random.randint
from Monster import Monster  # code uses Monster.Monster
from Weapon import Weapon  # code uses Weapon.Weapon


class Vampire(Monster):
    """A Blood-thirsty monster looking for its next meal

    ChildClass of Monster
    """

    def __init__(self):
        """Constructor for Vampire class"""

        self.name = "Vampire"
        super().__init__(self.name, randint(100, 200), randint(10, 20))

    def damage(self, weapon: Weapon, atk: int):
        """Overrides Monster class damage method to incorporate immunity to chocolate bars

            Parameters:
            weapon - Weapon uses to attack monster
            atk - player's attack power
        """

        if weapon.name == "Chocolate Bar":
            self.health += 0
        else:
            self.health -= atk * weapon.mod
            if self.health <= 0:
                self.home.resurrect(self)
