from Weapon import Weapon  # code uses Weapon.Weapon


class Monster:
    """A Monster has replaced each of your neighbors"""

    def __init__(self, name, hp, atk):
        """Constructor for the Monster class

        Parameters:
        name - Monster's name
        hp - Monster's health level
        atk - Monsters's attack power
        """

        self.name = name
        self.health = hp
        self.attack = atk
        self.home = None

    def damage(self, weapon: Weapon, atk : int):
        """Standard damage method when Monster is attacked

            Parameters:
            weapon - Weapon uses to attack monster
            atk - player's attack power
        """

        self.health -= atk * weapon.mod
        if self.health <= 0:
            self.home.resurrect(self)
