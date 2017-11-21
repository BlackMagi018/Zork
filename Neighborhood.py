from Home import Home
from random import randint


class Neighborhood:

    def __init__(self):
        grid = []
        houses = randint(3, 6)
        last = None
        for i in range(0, houses):
            current = Home()
            if last is not None:
                last.right = current
                current.left = last
                grid.append(last)
            last = current
