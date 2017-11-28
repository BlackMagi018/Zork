from random import randint  # code uses random.randint
from Monster import Monster  # code uses Monster.Monster
from Weapon import Weapon  # code uses Weapon.Weapon


class Zombie(Monster):
    """A Mindless creatures hungry for flesh shuffles towards you"""

    def __init__(self):
        """Constructor for Zombie class"""

        self.name = "Zombie"
        super().__init__(self.name, randint(50, 100), randint(0, 10))

    def damage(self, weapon: Weapon, atk: int):
        """Overrides Monster class damage method to incorporate vulnerability to sour straws

                    Parameters:
                    weapon - Weapon uses to attack monster
                    atk - player's attack power
                """

        if weapon.name == "Sour Straws":
            self.health -= atk * 5
            if self.health <= 0:
                self.home.resurrect(self)
        else:
            self.health -= atk * weapon.mod
            if self.health <= 0:
                self.home.resurrect(self)
