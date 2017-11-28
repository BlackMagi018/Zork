from random import uniform  # code uses random.uniform
from Weapon import Weapon  # code uses Weapon.Weapon


class ChocolateBar(Weapon):
    """A Chocolaty bar of goodness filled with Cocoa power

        ChildClass of Weapon
        """

    def __init__(self):
        """Constructor for Chocolate Bar class"""

        self.text = "Chocolate Bar"
        self.mod = round(uniform(2, 2.4),2)
        self.ammo = 4
        super().__init__(self.text, self.mod, self.ammo)
