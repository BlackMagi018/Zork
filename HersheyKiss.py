from Weapon import Weapon


class HersheyKiss(Weapon):

    def __init__(self):
        text = "Hershey Kiss"
        mod = 1
        ammo = -1
        super().__init__(text, mod, ammo)
