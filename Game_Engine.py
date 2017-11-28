from Monster import Monster  # codee uses Monster.Monster
from Player import Player  # code uses Player.Player
from Neighborhood import Neighborhood  # code uses Neighborhood.Neighborhood
from Home import Home  # code uses Home.Home


class Game_Engine:
    """Runs the Zork Games and handles the logic"""

    def __init__(self):
        """Constructor for the Game_Engine class"""

        self.player = Player()
        self.Map = Neighborhood()
        self.player.location = self.Map.grid.__getitem__(0)
        self.GameOver = False

    def enterHouse(self):
        """Initiates fight mechanic with monsters in house"""

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
                if self.GameOver:
                    print("All your neighbors rejoice as the Hallow's Eve Curse has been lifted from everyone")
                    print("Congratulations! You WIN")
                    fighting = False
                else:
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
        """Moves player to the house to the left"""

        assert isinstance(self.player.location, Home)
        if self.player.location.left is not None:
            self.player.location = self.player.location.left
        else:
            print("The player can't move left")

    def moveRight(self):
        """Moves player to the house to the right"""

        assert isinstance(self.player.location, Home)
        if self.player.location.right is not None:
            self.player.location = self.player.location.right
        else:
            print("The player can't move right")

    def getHouseStatus(self):
        """Prints the Home's Monster Pop and Monster Info"""

        print("House Population: " + str(self.player.location.population))
        for monsters in self.player.__location.thrall:
            if Monster.__instancecheck__(monsters):
                print(str(monsters.name) + ": Health: " + str(monsters.health))
        print(" ")

    def getPlayerStatus(self):
        """Prints player stats and arsenal contents"""

        print("Health: ", self.player.__getattribute__("health"))
        print("Attack: ", self.player.__getattribute__("attack"))
        print("Arsenal:")
        i = 1
        for weapon in self.player.arsenal:
            print(str(i) + ": Name: " + weapon.name + " Mod: " + str(weapon.mod) + " Ammo: " + str(weapon.ammo))
            i += 1
        print(" ")

    def getMapStatus(self):
        """Prints data on the entire neighborhood"""

        i = 1
        print("Current House: House " + str(self.Map.grid.index(self.player.location) + 1))
        for house in self.Map.grid:
            print("House " + str(i) + ": Monster Population " + str(house.population))
            i += 1

    def getHelp(self):
        """Prints Help screen"""

        print("enter house - enter the current house")
        print("move left - move to the next house to your left if possible")
        print("move right - move to the next house to your right if possible")
        print("player status - get the current status of player character")
        print("house status - get the current status of the current house")
        print('show map - get the current info on neighbor hood')
        print("help - pulls up help sheet")
        print("quit - end the game\n")

    def checkPop(self):
        """Check to see if all monsters are defeated"""

        if self.Map.totalMonsters == 0:
            self.GameOver = True

    def intro(self):
        """Prints intro text"""

        print("Welecome to Zork\n")
        print("It seemed like a normal Halloween Eve. You bought a lot of candy, ate a lot of candy" +
              " and went to bed early. You had a lot trick-or-treating to do the next day.\n" +
              "Unfortunately, when you woke up you discovered that the world was not how you left it."
              "Batches of bad candy had transformed your friends and neighbors into all sorts\nof crazy monsters. "
              "Somehow you missed the tainted candy; it is therefore up to you to save your neighborhood "
              "and turn everyone back to normal.\n")

    def Command(self, command):
        """Reads inputs for accepted commands"""

        if command == "enter house":
            self.enterHouse()
        elif command == "move left":
            self.moveLeft()
        elif command == "move right":
            self.moveRight()
        elif command == "player status":
            self.getPlayerStatus()
        elif command == "house status":
            self.getHouseStatus()
        elif command == "help":
            self.getHelp()
        elif command == "quit":
            self.GameOver = True
        elif command == "show map":
            self.getMapStatus()
        else:
            print("Invalid Entry")
            self.getHelp()


"""Starts the Zork Game"""
if __name__ == '__main__':
    Game = Game_Engine()
    Game.intro()
    Game.checkPop()
    while not Game.GameOver:
        text = input("What would you like to do\n")
        text.lower()
        Game.Command(text)
    print("Goodbye")
