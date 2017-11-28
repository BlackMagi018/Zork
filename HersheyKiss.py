from Weapon import Weapon  # code uses Weapon.Weapon


class HersheyKiss(Weapon):
    """Immense power lies with this chocolate kiss of death

            ChildClass of Weapon
            """

    def __init__(self):
        """Constructor for HersheyKiss class"""

        self.text = "Hershey Kiss"
        self.mod = 1
        self.ammo = -1
        super().__init__(self.text, self.mod, self.ammo)
