

class MADNExtreme:
    gamestates = ["initializing","running","ending","setup"]
    currentState = gamestates[3]
    def initialize(self):
        print("Initializing Game")
        self.board=Board()
        self.board.generateBoard()

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

        self.currentState = self.gamestates[0]

    
    def checkForGameSetupConstraints(self):
        if self.playerCount > 8 or self.playerCount < 2:
            return False
        if self.boardSize > 4 or self.boardSize < 1:
            return False
        if self.difficulty > 10 or self.difficulty < 0:
            return False
        return True

class Board:
    def generateBoard(self):
        self.houses = []
        self.board = []
        for player in range(game.playerCount):
            self.houses.append(input("Please enter Playername: "))
        for spot in self.houses:
            for i in range(4 * (game.boardSize * 4 )):
                self.board.append(0)
        for i in range(game.playerCount):
            self.board[i * 4 + game.boardSize * 4] = 1

    def printBoard(self):
        for i in self.board:
            print(i)

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
game.initialize()
game.board.printBoard()

