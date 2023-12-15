class Board:
    def __init__(self, player_count):
        self.player_count=player_count
        self.houses=[]
        self.homes=[]
        self.field=[]

    def getPlayersHomes(self, playerColor):
        return self.houses[playerColor-1]

    def setPlayersHouseFiguresInEntrypoint(self, player, game):
        
        figure = self.houses[player-1][len(self.houses[player-1])-1]
        self.houses[player-1][0].setFigureIn(figure)

    def checkForFreeEntryPoint(self, player):
        return self.field[player].isEmpty()
    
    def print(self):
        print()
        for house in self.houses:
            for spot in house:
                spot.print()
        print("\n^^^^^^\nhouse\n")
        for home in self.homes:
            for spot in home:
                spot.print()
        print("\n^^^^^^\nhome\n")
        for field in self.field:
            field.print()
        print("\n^^^^^^\nfield\n")


