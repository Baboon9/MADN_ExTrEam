import unittest

class GameMethodsTests(unittest.TestCase):

        def test_arrayLengths(self):
            self.assertTrue(len(game.figures) == game.player_count*4, "Figure Length Wrong!") 
            self.assertTrue(len(game.board.houses) == game.player_count, "Houses Length not correct!" )
            self.assertTrue(len(game.board.homes) == game.player_count, "Player Count not correct!" )
            self.assertTrue(len(game.board.field) == game.player_count  *12, "Game Field length is not right!" )
            self.assertTrue(len(game.figures) == game.player_count *4, "The amount of Figures is not correct!" )


class Game:
    def __init__(self):
        self.game_states = ["initializing","starting","running","stopping","ending"]
        self.game_state = self.game_states[0]
        self.player_count = int(input("How many players are there? Enter a number from 1-8: "))
        self.board = Board(self.player_count)
        
        self.figures = []
        self.players = []
        
        for i in range(0,self.player_count):
            self.players.append(Player(str(input("Enter your name: ")),i+1))

        for player in self.players:
            for j in range (0,4):
                self.figures.append(Figure(player.color))

        self.board.generateBoard(self.player_count)
        
        

        self.computer_player_count = int(input("Against how many Computer players do you want to play? Enter a number between 0-4: "))
        
        self.start()


    def start(self):
        print("Game is starting..")
        self.game_state = self.game_states[1]
        self.board.setInFigures(self.player_count, self.figures)
        self.game_state = self.game_states[2]

        self.run()

    def run(self):
        print("Game is running..")
        print("printing board..")
        self.print()
        #while self.game_state == self.game_states[2]:
        #    pass

    def print(self):
        self.board.print()


class Board:
    def __init__(self, player_count):
        self.player_count=player_count
        self.houses=[]
        self.homes=[]
        self.field=[]


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


    def generateBoard(self, player_count):
        for i in range(0,self.player_count):
            self.houses.append([])  

        for i in range(0,4):
            for house in self.houses:
                house.append(Spot(None))

        for i in range(0,self.player_count):
            self.homes.append([])

        for i in range(0,4):
            for home in self.homes:
                home.append(Spot(None))

        for i in range(0,12*self.player_count):
            self.field.append(Spot(None) )
    

    def setInFigures(self,player_count,figures):
        for i in range(0,player_count):
            for j in range(0,4*player_count):
                self.houses[i][int(j/player_count)].setInFigure(figures[j])

        for spot in self.houses:
            print(spot)    


class Figure:
    def __init__(self, color):
        self.color = color
    def getFigureOfColorAsInt(self,integer):
        if self.color == integer:
            return self

class Spot:
    def __init__(self, figure):
        self.figureAtSpot = figure
    def setInFigure(self, figure):
        self.figureAtSpot = figure
    def print(self):
        if not self.figureAtSpot == None:
            print(self.figureAtSpot.color,end="")
        else:
            print("O",end="")


class Player:
    def __init__(self, name, color):
        self.name=name
        self.color=color

class Computer:
    def __init__(self):
        pass

class Home:
    def __init__(self):
        pass

class House:
    def __init__(self):
        pass

class Field:
    def __init__(self):
        pass

class Network:
    def __init__(self):
        pass


game = Game()

test = GameMethodsTests()

unittest.main()
