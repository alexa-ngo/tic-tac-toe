from board import Board
from game import Game
from player import *

alexa = Player("x")
riley = Player("o")

the_board = Board(alexa, riley)

# TEMPLATEEEEEEEEEEEEE
# the_board.set_pos()
# the_board.set_pos()
# the_board.new_round()
# the_board.set_pos()
# the_board.set_pos()
# the_board.new_round()
# the_board.set_pos()
# the_board.set_pos()
# the_board.new_round()
# the_board.set_pos()
# the_board.set_pos()

# The X will win!
the_board.set_pos(0)
the_board.set_pos(1)
the_board.new_round()
the_board.set_pos(2)
the_board.set_pos(3)
the_board.new_round()
the_board.set_pos(4)
the_board.set_pos(5)
the_board.new_round()
the_board.set_pos(8)
the_board.set_pos(6)
the_board.set_pos(7)

# THERE WILL BE A TIE!!!!!!
# the_board.set_pos()
# the_board.set_pos()
# the_board.new_round()
# the_board.set_pos()
# the_board.set_pos()
# the_board.new_round()
# the_board.set_pos()
# the_board.set_pos()
# the_board.new_round()
# the_board.set_pos()
# the_board.set_pos()

# THE "X" will WIN!!!!!!!!
# the_board.set_pos(4)
# the_board.set_pos(0)
# the_board.new_round()
# the_board.set_pos(6)
# the_board.set_pos(2)
# the_board.new_round()
# the_board.set_pos(7)
# the_board.set_pos(3)
# the_board.new_round()
# the_board.set_pos(8)
# the_board.set_pos(5)

# THE "O" will WIN!!!!!!!!
# the_board.set_pos(1)
# the_board.set_pos(0)
# the_board.new_round()
# the_board.set_pos(2)
# the_board.set_pos(3)
# the_board.new_round()
# the_board.set_pos(4)
# the_board.set_pos(5)
# the_board.new_round()
# the_board.set_pos(8)
# the_board.set_pos(6)


the_board.print_board()

alexa_game = Game(the_board, alexa, riley)

# Check if there is three in a row
print(alexa_game.check(the_board))

# Check if there is a tie
print(alexa_game.is_tied())

