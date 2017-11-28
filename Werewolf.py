from random import randint  # code uses random.randint
from Monster import Monster  # code uses Monster.Monster
from Weapon import Weapon  # code uses Weapon.Weapon


class Werewolf(Monster):

    def __init__(self):
        """Constructor for Werewolf class

        ChildClass of Monster
        """

        self.name = "Werewolf"
        super().__init__(self.name, 200, randint(0, 40))

    def damage(self, weapon: Weapon, atk: int):
        """Overrides Monster class damage method to incorporate immunity to chocolate bars and sour straqs

                    Parameters:
                    weapon - Weapon uses to attack monster
                    atk - player's attack power
                """

        if weapon.name == "Chocolate Bar" or weapon.name == "Sour Straws":
            self.health -= 0
        else:
            self.health -= atk * weapon.mod
            if self.health <= 0:
                self.home.resurrect(self)
