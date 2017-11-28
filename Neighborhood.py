from Ghouls import Ghouls
from Werewolves import Werewolves
from Vampire import Vampire
from Home import Home
from Persons import Persons
from Zombies import Zombies
from random import randint


class Neighborhood:

    totalMonsters = 0

    def __init__(self):
        self.grid = []
        houses = randint(3, 6)
        last = None
        for i in range(0, 1):
            current = Home()
            self.createMonster(current)
            current.grid = self
            self.grid.append(current)
            # if last is not None:
            #     last.right = current
            #     current.left = last
            #     self.grid.append(last)
            # last = current

    def createMonster(self, house: Home):
        x = randint(1, 5)
        house.population = x
        for i in range(0, 1):
            m_type = randint(0, 0)
            if m_type == 0:
                house.population -= 1
                monster = Persons()
                monster.home = house
                house.thrall.append(monster)
            elif m_type == 1:
                monster = Zombies()
                monster.home = house
                house.thrall.append(monster)
            elif m_type == 2:
                monster = Vampire()
                monster.home = house
                house.thrall.append(monster)
            elif m_type == 3:
                monster = Ghouls()
                monster.home = house
                house.thrall.append(monster)
            elif m_type == 4:
                monster = Werewolves()
                monster.home = house
                house.thrall.append(monster)
        self.totalMonsters += house.population

