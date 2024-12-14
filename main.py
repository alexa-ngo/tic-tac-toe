from board import Board
from game import Game
from player import *

alexa = Player("x")
riley = Player("o")

the_board = Board(alexa, riley)
the_board.set_pos(3)
the_board.set_pos(2)
the_board.new_round()
the_board.set_pos(5)
the_board.set_pos(4)
the_board.new_round()
the_board.set_pos(1)
the_board.set_pos(7)
the_board.new_round()


the_board.iterate_through_board()

alexa_game = Game(the_board, alexa, riley)
print(alexa_game.check(the_board))