

class MADNExtreme:
    gamestates = ["initializing","running","ending","setup"]
    currentState = gamestates[3]
    def initialize():
        print("Initializing Game")
        pass
    def run():
        pass
    def end():
        pass
    def setup(self):
        print("How many players? (max 8)")
        self.playerCount=int(input())
        print("What boardsize? (max 4)")
        self.boardSize=int(input())
        print("What difficulty? (0-10")
        self.difficulty=int(input())
        print("Game has been Setup with the parameters Playercount, Boardsize, and Difficulty")
        if (not self.checkForGameSetupConstraints()):
            print("You need to set reasonable parameters..")
            self.setup()

        self.currentState = gameStates[0]

    
    def checkForGameSetupConstraints(self):
        if self.playerCount > 8 or self.playerCount < 2:
            return False
        if self.boardSize > 4 or self.boardSize < 1:
            return False
        if self.difficulty > 10 or self.difficulty < 0:
            return False
        return True

class Board:
    pass

class Network:
    pass

class Player:
    pass



game = MADNExtreme()

print("Available Game States:")
print(game.gamestates)
print("Current Game State:")
print(game.currentState)
game.setup()



