from random import randint
from Monster import Monster


class Zombies(Monster):

    def __init__(self):
        super().__init__(randint(50, 100), randint(0, 10))
