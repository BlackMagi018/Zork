from random import uniform  # code uses random.uniform
from Weapon import Weapon  # code uses Weapon.Weapon


class SourStraws(Weapon):
    """The sour straws with a punch

    ChildClass of Weapon
    """

    def __init__(self):
        """Constructor for SourStraws class"""

        self.name = "Sour Straws"
        self.mod = round(uniform(1, 1.75),2)
        self.ammo = 2
        super().__init__(self.name, self.mod, self.ammo)
