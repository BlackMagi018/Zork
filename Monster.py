from Weapon import Weapon


class Monster:

    def __init__(self, name, hp, atk):
        self.name = name
        self.health = hp
        self.attack = atk
        self.home = None

    def damage(self, weapon: Weapon, atk : int):
        self.health -= atk * weapon.mod
        if self.health <= 0:
            self.home.resurrect(self)
