from Ghouls import Ghouls
from Werewolves import Werewolves
from Vampire import Vampire
from Home import Home
from Persons import Persons
from Zombies import Zombies
from random import randint


class Neighborhood:

    def __init__(self):
        self.grid = []
        houses = randint(3, 6)
        last = None
        for i in range(0, houses):
            current = Home()
            self.createMonster(current)
            if last is not None:
                last.right = current
                current.left = last
                self.grid.append(last)
            last = current

    def createMonster(self, house: Home):
        x = randint(0, 10)
        for i in range(0, x):
            type = randint(0, 4)
            if type == 0:
                monster = Persons()
                monster.home = house
                house.thrall.append(monster)
            elif type == 1:
                monster = Zombies()
                monster.home = house
                house.thrall.append(monster)
            elif type == 2:
                monster = Vampire()
                monster.home = house
                house.thrall.append(monster)
            elif type == 3:
                monster = Ghouls()
                monster.home = house
                house.thrall.append(monster)
            elif type == 4:
                monster = Werewolves()
                monster.home = house
                house.thrall.append(monster)
