from Monster import Monster
from Player import Player
from Neighborhood import Neighborhood
from Home import Home
from Weapon import Weapon


class Game:
    def __init__(self):
        self.player = Player()
        self.Map = Neighborhood()
        self.player.location = self.Map.grid.__getitem__(0)
        self.GameOver = False

    def getHouseStatus(self):
        for monsters in self.player.location.thrall:
            print(str(monsters.name) + ": Health: " + str(monsters.health))

    def getPlayerStatus(self):
        print("Health: ", self.player.health)
        print("Attack: ", self.player.attack)
        print("Arsenal:")
        i = 1
        for weapon in self.player.arsenal:
            print(str(i) + ": Name: " + weapon.name + " Mod: " + str(weapon.mod) + " Ammo: " + str(weapon.ammo))
            i = i + 1


if __name__ == '__main__':
    Game = Game()
    while not Game.GameOver:
        Game.getHouseStatus()
        Game.GameOver = True
    print("Done")
