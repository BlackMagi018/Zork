from Weapon import Weapon


class HersheyKiss(Weapon):

    def __init__(self):
        self.text = "Hershey Kiss"
        self.mod = 1
        self.ammo = -1
        super().__init__(self.text, self.mod, self.ammo)
