from random import randint  # code uses random.randint
from Ghouls import Ghouls  # code uses Ghouls.Ghouls
from Home import Home  # code uses Home.Home
from Person import Person  # code uses Person.Person
from Vampire import Vampire  # code uses Vampire.Vampire
from Werewolf import Werewolf  # code uses Werewolf.Werewolf
from Zombie import Zombie  # code uses Zombie.Zombie


class Neighborhood:
    """The Neighborhood that you lived is has gone through a grim transformation

    Attributes:
        totalMonsters - total count of monsters in all the homes
        grid - list of all the home objects
    """

    totalMonsters = 0

    def __init__(self):
        """Constructor for Neighborhood class

        Creates a random number of homes in neighborhood and connects them
        """

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
        """Method randomly creates and inserts monsters in each home

            Parameters
            house - Home object
        """

        x = randint(1, 5)
        house.population = 0
        for i in range(0, x):
            m_type = randint(0, 4)
            if m_type == 0:
                monster = Person()
                monster.home = house
                house.thrall.append(monster)
            elif m_type == 1:
                house.population += 1
                monster = Zombie()
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
                monster = Werewolf()
                monster.home = house
                house.thrall.append(monster)
        self.totalMonsters += house.population
