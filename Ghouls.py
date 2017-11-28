from random import randint  # code uses random.randint
from Monster import Monster  # code uses Monster.Monster
from Weapon import Weapon  # code uses Weapon.Weapon


class Ghouls(Monster):
    """Evil Magic has summoned forth a creatures that finds your flesh a delicacy

    ChildClass of Monster
    """

    def __init__(self):
        """Constructor for the Ghoul Class"""

        self.name = "Ghoul"
        super().__init__(self.name, randint(40, 80), randint(15, 30))

    def damage(self, weapon: Weapon, atk: int):
        """Overrides Monster class damage method to incorporate a weakness for Nerd Bombs

            Parameters:
            weapon - Weapon uses to attack monster
            atk - player's attack power
        """

        if weapon.name == "Nerd Bombs":
            self.health -= atk * 5
            if self.health <= 0:
                self.home.resurrect(self)
        else:
            self.health -= atk * weapon.mod
            if self.health <= 0:
                self.home.resurrect(self)
