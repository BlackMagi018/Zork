from Monster import Monster
from Weapon import Weapon


class Person(Monster):
    """A cured neighbor that will be charitable for your effort

    ChildClass of Monster
    """

    def __init__(self):
        """Constructor for Person class"""

        self.name = "Person"
        super().__init__(self.name, 100, -1)

    def damage(self, weapon: Weapon, atk: int):
        """Override Monster damage method, Person takes no damage

            Parameters:
            weapon - Weapon uses to attack monster
            atk - player's attack power
        """

        self.health += 0
