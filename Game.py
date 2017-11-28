from Player import Player
from Neighborhood import Neighborhood
from Home import Home


class Game:
    def __init__(self):
        self.player = Player()
        self.Map = Neighborhood()
        self.player.location = self.Map.grid.__getitem__(0)
        self.GameOver = False

    def enterHouse(self):
        fighting = True
        print("Wild Monsters have appeared")
        while fighting is True:
            text = input("Attack or Retreat\n")
            if text.lower() == "retreat":
                print("You have fled the house")
                fighting = False
            elif text.lower() == "attack":
                text = input("Choose an Weapons # to Use\n")
                i = int(text)-1
                candy = self.player.useWeapon(i)
                self.player.location.damage(candy, self.player.attack)
                self.checkPop()
                self.player.location.revenge(self.player)
                if self.player.health <= 0:
                    print("Your efforts though valiant were not enough you were consumed by your former neighbors")
                    self.GameOver = True
                    fighting = False
                else:
                    print("Player Health: " + str(self.player.health))
            else:
                print("Invalid Entry")

    def moveLeft(self):
        assert isinstance(self.player.location, Home)
        if self.player.location.left is not None:
            self.player.location = self.player.location.left
        else:
            print("The player can't move left")

    def moveRight(self):
        assert isinstance(self.player.location, Home)
        if self.player.location.right is not None:
            self.player.location = self.player.location.right
        else:
            print("The player can't move right")

    def getHouseStatus(self):
        print("House Population: " + str(self.player.location.population))
        for monsters in self.player.location.thrall:
            print(str(monsters.name) + ": Health: " + str(monsters.health))
        print(" ")

    def getPlayerStatus(self):
        print("Health: ", self.player.health)
        print("Attack: ", self.player.attack)
        print("Arsenal:")
        i = 1
        for weapon in self.player.arsenal:
            print(str(i) + ": Name: " + weapon.name + " Mod: " + str(weapon.mod) + " Ammo: " + str(weapon.ammo))
            i = i + 1
        print(" ")

    def checkPop(self):
        if self.Map.totalMonsters == 0:
            self.GameOver = True


if __name__ == '__main__':
    Game = Game()
    Game.checkPop()
    while not Game.GameOver:
        Game.getPlayerStatus()
        Game.enterHouse()
        Game.GameOver = True
    print("Done")
