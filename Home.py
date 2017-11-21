from random import randint
from Ghouls import Ghouls
from Werewolves import Werewolves
from Vampire import Vampire
from Persons import Persons
from Zombies import Zombies


class Home:
    """A seemingly normal house is hiding pure horror waiting to attack"""

    def __init__(self):
        self.thrall = []
        self.left = None
        self.right = None
        x = randint(0, 10)
        for i in range(0, x):
            monster = randint(0, 4)
            if monster == 0:
                self.thrall.append(Persons)
            elif monster == 1:
                self.thrall.append(Zombies)
            elif monster == 2:
                self.thrall.append(Vampire)
            elif monster == 3:
                self.thrall.append(Ghouls)
            elif monster == 4:
                self.thrall.append(Werewolves)
