from random import randint  # code uses random.randint
from HersheyKiss import HersheyKiss  # code uses HersheyKiss.HersheyKiss
from SourStraws import SourStraws  # code uses SoursStraws.SourStraws
from ChocolateBar import ChocolateBar  # code uses ChocolateBar.ChocolateBar
from NerdBombs import NerdBombs  # code uses NerdBombs.NerdBombs


class Player:
    """The sole survivor tasked with saving their neighborhood from sugar-tainted monsters

        Attributes:
        health - Players health level
        attack - Players attack power
        arsenal - list of player's weapons
        location - current location of player
    """

    health = randint(100, 125)
    attack = randint(10, 20)
    arsenal = []
    location = None

    def __init__(self):
        """Constructor for the Player class"""

        x = HersheyKiss()
        self.arsenal.append(x)
        for i in range(0, 9):
            c = randint(0, 2)
            if c == 0:
                x = SourStraws()
            elif c == 1:
                x = ChocolateBar()
            else:
                x = NerdBombs()
            self.arsenal.append(x)

    def useWeapon(self, i: int):
        """Method to use a weapon currently in your arsenal"""

        try:
            x = self.arsenal[i]
        except IndexError:
            x = self.arsenal[0]
        x.ammo -= 1
        if x.ammo > 0:
            self.arsenal.__setitem__(i, x)
        elif x.ammo == 0:
            self.arsenal.remove(x)
        else:
            pass
        print("You attacked with " + x.name)
        return x
