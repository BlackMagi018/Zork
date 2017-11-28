from random import randint
from Ghouls import Ghouls
from Home import Home
from Persons import Persons
from Vampire import Vampire
from Werewolves import Werewolves
from Zombies import Zombies


class Neighborhood:
    totalMonsters = 0

    def __init__(self):
        self.grid = []
        houses = randint(3, 6)
        last = None
        for i in range(0, houses):
            current = Home()
            self.createMonster(current)
            current.grid = self
            if last is not None:
                last.right = current
                current.left = last
                self.grid.append(last)
            last = current

    def createMonster(self, house: Home):
        x = randint(1, 5)
        house.population = 0
        for i in range(0, x):
            m_type = randint(0, 4)
            if m_type == 0:
                monster = Persons()
                monster.home = house
                house.thrall.append(monster)
            elif m_type == 1:
                house.population += 1
                monster = Zombies()
                monster.home = house
                house.thrall.append(monster)
            elif m_type == 2:
                house.population += 1
                monster = Vampire()
                monster.home = house
                house.thrall.append(monster)
            elif m_type == 3:
                house.population += 1
                monster = Ghouls()
                monster.home = house
                house.thrall.append(monster)
            elif m_type == 4:
                house.population += 1
                monster = Werewolves()
                monster.home = house
                house.thrall.append(monster)
        self.totalMonsters += house.population
