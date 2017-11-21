from random import randint
from Monster import Monster


class Werewolves(Monster):

    def __init__(self):
        super().__init__(200, randint(0, 40))
