from board import Board
from player import *

alexa = Player("x")
riley = Player("o")

print("Alexa's role:" , alexa.get_player_role())
print("Riley's role:", riley.get_player_role())

alexa.swap_player_role()
riley.swap_player_role()

print("Alexa's role2:" , alexa.get_player_role())
print("Riley's role2:", riley.get_player_role())

# def set_pos(self, index_of_array):
#     if self._board[index_of_array] is not None:
#         print("Sorry, the position is occupied!")
#     else:
#
# board = Board(x, o)
#
# print("First: ")
# board.set_pos(5)
#
# print("\nSecond: ")
# board.set_pos(1)
#
# print("\nThird: ")
# board.set_pos(0)
#
