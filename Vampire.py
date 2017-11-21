from random import randint
from Monster import Monster


class Vampire(Monster):

    def __init__(self):
        super().__init__(randint(100, 200), randint(10, 20))
