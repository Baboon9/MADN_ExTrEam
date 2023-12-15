import Game.game as Game
import Game.board as Board
import Game.field as Field
import Game.figure as Figure
import Game.home as Home
import Game.player as Player

menu = Game.Menu()
setup = menu.get_setup()

game = Game.Game(setup)
field = Field.Field()
#board = Board.Board() 
#board.generate_board()

