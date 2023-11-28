import unittest
import random

class GameMethodsTests(unittest.TestCase):

        def test_arrayLengths(self):
            self.assertTrue(len(game.figures) == game.player_count*4, "Figure Length Wrong!") 
            self.assertTrue(len(game.board.houses) == game.player_count, "Houses Length not correct!" )
            self.assertTrue(len(game.board.homes) == game.player_count, "Player Count not correct!" )
            self.assertTrue(len(game.board.field) == game.player_count  *12, "Game Field length is not right!" )
            self.assertTrue(len(game.figures) == game.player_count *4, "The amount of Figures is not correct!" )
        
        def test_gameArchitecture(self):
            self.assertTrue(game.checkForPlayerAtTurn() == 1)
            self.assertTrue(game.chekForGameOver() == False)
            self.assertTrue(game.rollTheDice() <= 1 or game.rollTheDice() >= 6)
            self.assertTrue(game.checkForPlayerFigureAvailability() == False)



class Game:
    def checkForGameOver(self):
        print("Checking weather the game is over or not..")
        if self.game_over:
            print("The game is in deed over.")
            self.game_state = self.game_state[4]
        else:
            print("The game is not over yet.")
    
    def checkForPlayerAtTurn(self):
        print("Player", self.player_at_turn, "is at turn.")
    
    def rollTheDice(self):
        print("Rolling the dice..")
        die = random.randrange(1,7)
        print("The dice rolled as",die,"eyes.")
        return die

    def moveFigure(self):
        pass

    def checkFigureCollision(self, spot1, spot2):
        print("Checking for collision..")
        isCollided = not spot1.isEmpty() and not spot2.isEmpty()
        print("Collision status:",isCollided)
        return isCollided

    def setFigureInField(self):
        print("You rolled a 6, so you have to put a figure in the field, if your entry point is free.")
        self.board.checkForFreeEntryPoint(self.player_at_turn)
        entrypoint = self.board.field[self.player_at_turn]
        self.checkFigureCollision(entrypoint,entrypoint)
        self.board.setPlayersHouseFiguresInEntrypoint(self.player_at_turn, self)

    def letPlayerDoHisTurn(self):
        print("Now it is the players turn.")
        #Lets wonder weather the player has to roll once or up to thrice
        if not self.checkForPlayerFigureAvailability():
            #may roll thrice
            diceRolled = 0
            while diceRolled < 3:
                die = self.rollTheDice()
                diceRolled = diceRolled +1
                if die == 6:
                    self.setFigureInField()
                    self.endPlayersTurn()
        else:
            print("What figure do you want to move?")
            figureToMove = int(input())
            die = self.rollTheDice()
            self.moveFigure(figureToMove, die)
            self.checkFigureCollision(figureToMove)
            self.endPlayersTurn()

    def checkForPlayerFigureAvailability(self):
        print("Checking the players house weather it is full or not.")
        if self.players[self.player_at_turn].checkForAvailableFigures(self.board):
            print("The house is in deed full.")
            return False
        else:
            print("There are figures on the field.")
            return True

    def checkForPlayerHasWon(self):
        pass

    def endPlayersTurn(self):
        self.player_at_turn = self.player_at_turn +1
        self.player_at_turn = self.player_at_turn % self.player_count
        input("Press Enter to end your turn.")

    def gameOver(self):
        pass

    def newGame(self):
        pass

    def showCredits(self):
        Print("This Game was made by Tim-Ohle Schürheck, thanks for playing!")

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
        self.game_over = False
        self.player_at_turn = 1
        while self.game_state == self.game_states[2]:
            #Has the game been finished, is it over?
            self.checkForGameOver()
            if self.game_state == self.game_states[4]:
                self.showCredits()
                self.newGame()

            #Lets see who is at turn.
            self.checkForPlayerAtTurn()
            
            #Now let that player do his turn.
            self.letPlayerDoHisTurn()

            #Finally end that players turn.
            self.endPlayersTurn()

            #Okay, so I wonder weather he has won yet.
            self.checkForPlayerHasWon()

            

                
    def print(self):
        self.board.print()


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
                self.houses[i][int(j/player_count)].setFigureIn(figures[j])

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
        self.figure_at_spot = figure
    def getFigure(self):
        return self.figure_at_spot
    def setFigureIn(self, figure):
        self.figure_at_spot = figure
    def print(self):
        if not self.figure_at_spot == None:
            print(self.figure_at_spot.color,end="")
        else:
            print("O",end="")
    def removeFigure(self, figure):
        self.figure_at_spot = None
    def isEmpty(self):
        return self.figure_at_spot == None

class Player:
    def __init__(self, name, color):
        self.name=name
        self.color=color

    def checkForAvailableFigures(self, board):
        if len(board.getPlayersHomes(self.color)) == 4:
            return True
        else:
            return False

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
