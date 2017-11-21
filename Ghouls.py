from random import randint
from Monster import Monster


class Ghouls(Monster):

    def __init__(self):
        super().__init__(randint(40, 80), randint(15, 30))
