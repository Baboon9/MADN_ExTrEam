import random


class Game:
    def __init__(self,setup):
        self.player_count=setup[0]
        self.difficulty=setup[1]
        self.board_size=setup[2]

    def check_forGameOver(self):
        print("Checking weather the game is over or not..")
        if self.game_over:
            print("The game is in deed over.")
            self.game_state = self.game_state[4]
        else:
            print("The game is not over yet.")
    
    def check_forPlayerAtTurn(self):
        print("Player", self.player_at_turn, "is at turn.")
    
    def roll_dice(self):
        print("Rolling the dice..")
        die = random.randrange(1,7)
        print("The dice rolled as",die,"eyes.")
        return die

    def move_figure(self):
        pass

    def check_figureCollision(self, spot1, spot2):
        print("Checking for collision..")
        isCollided = not spot1.isEmpty() and not spot2.isEmpty()
        print("Collision status:",isCollided)
        return isCollided

    def set_figureInField(self):
        print("You rolled a 6, so you have to put a figure in the field, if your entry point is free.")
        self.board.checkForFreeEntryPoint(self.player_at_turn)
        entrypoint = self.board.field[self.player_at_turn]
        self.check_figureCollision(entrypoint,entrypoint)
        self.board.setPlayersHouseFiguresInEntrypoint(self.player_at_turn, self)

    def letPlayerDoHisTurn(self):
        print("Now it is the players turn.")
        #Lets wonder weather the player has to roll once or up to thrice
        if not self.check_playerAvailability():
            #may roll thrice
            diceRolled = 0
            while diceRolled < 3:
                die = self.roll_dice()
                diceRolled = diceRolled +1
                if die == 6:
                    self.set_figureInField()
                    self.end_playersTurn()
        else:
            print("What figure do you want to move?")
            figureToMove = int(input())
            die = self.roll_dice()
            self.move_figure(figureToMove, die)
            self.check_figureCollision(figureToMove)
            self.end_playersTurn()

    def check_playerAvailability(self):
        print("Checking the players house weather it is full or not.")
        if self.players[self.player_at_turn].checkForAvailableFigures(self.board):
            print("The house is in deed full.")
            return False
        else:
            print("There are figures on the field.")
            return True

    def check_playerHasWon(self):
        pass

    def end_playersTurn(self):
        self.player_at_turn = self.player_at_turn +1
        self.player_at_turn = self.player_at_turn % self.player_count
        input("Press Enter to end your turn.")

    def gameOver(self):
        print("Game is over now!")
        self.game_state=self.game_states[4]

    def new_game(self):
        print("starting new Game..")
        self.game_state=self.game_states[1]

    def show_credits(self):
        Print("This Game was made by Tim-Ohle Schürheck, thanks for playing!")

    def __init__(self):
        self.game_states = ["initializing","starting","running","stopping","ending"]
        self.game_state = self.game_states[0]
        self.player_count = int(input("How many players are there? Enter a number from 1-8: "))
        

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
            self.check_forGameOver()
            if self.game_state == self.game_states[4]:
                self.show_credits()
                self.new_game()

            #Lets see who is at turn.
            self.check_forPlayerAtTurn()
            
            #Now let that player do his turn.
            self.letPlayerDoHisTurn()

            #Finally end that players turn.
            self.end_playersTurn()

            #Okay, so I wonder weather he has won yet.
            self.check_playerHasWon()

            

                
    def print(self):
        self.board.print()

class Menu:
    def __init__(self):
        print("Setting up the game..")

    def ask_playerCount(self):
        return int(input("How many Players are in the game?"))

    def ask_difficulty(self):
        return int(input("What difficutly do you want to play="))

    def ask_boardSize(self):
        return int(input("How big should the Board be?"))
    
    def get_setup(self):
        return (self.ask_playerCount(), self.ask_difficulty(), self.ask_boardSize())
