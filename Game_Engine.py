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
                i = int(text) - 1
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
            if Monster.__instancecheck__(monsters):
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

    def getHelp(self):
        print("enter house - enter the current house")
        print("move left - move to the next house to your left if possible")
        print("move right - move to the next house to your right if possible")
        print("player status - get the current status of player character")
        print("house status - get the current status of the current house")
        print("help - pulls up help sheet\n")

    def checkPop(self):
        if self.Map.totalMonsters == 0:
            self.GameOver = True

    def intro(self):
        print("Welecome to Zork\n")
        print("It seemed like a normal Halloween Eve. You bought a lot of candy, ate a lot of candy" +
              " and went to bed early. You had a lot trick-or-treating to do the next day.\n" +
              "Unfortunately, when you woke up you discovered that the world was not how you left it."
              "Batches of bad candy had transformed your friends and neighbors into all sorts\nof crazy monsters. "
              "Somehow you missed the tainted candy; it is therefore up to you to save your neighborhood "
              "and turn everyone back to normal.\n")


    def Command(self,text):
        if text == "enter house":
            self.enterHouse()
        elif text == "move left":
            self.moveLeft()
        elif text == "move right":
            self.moveRight()
        elif text == "player status":
            self.getPlayerStatus()
        elif text == "house status":
            self.getHouseStatus()
        elif text == "help":
            self.getHelp()
        else:
            print("Invalid Entry")
            self.getHelp()


if __name__ == '__main__':
    Game = Game()
    Game.intro()
    Game.checkPop()
    while not Game.GameOver:
        text = input("What would you like to do\n")
        text.lower()
        Game.Command(text)
    print("Done")
