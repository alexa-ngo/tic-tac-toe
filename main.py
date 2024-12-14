from board import Board
from player import *

alexa = Player("x")
riley = Player("o")

the_board = Board(alexa, riley)
the_board.set_pos(1)
the_board.set_pos(0)
the_board.new_round()
the_board.set_pos(4)
the_board.set_pos(5)
the_board.new_round()