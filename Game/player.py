class Player:
    def __init__(self, name, color):
        self.name=name
        self.color=color

    def checkForAvailableFigures(self, board):
        if len(board.getPlayersHomes(self.color)) == 4:
            return True
        else:
            return False
