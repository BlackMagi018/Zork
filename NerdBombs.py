from random import uniform  # code uses random.uniform
from Weapon import Weapon  # code uses Weapon.Weapon


class NerdBombs(Weapon):
    """A meteoric explosion hides with this tiny piece of candy

    ChildClass of Weapon
    """

    def __init__(self):
        """Constructor for NerdBombs class"""

        self.text = "Nerd Bombs"
        self.mod = round(uniform(3.5, 5),2)
        self.ammo = 1
        super().__init__(self.text, self.mod, self.ammo)
