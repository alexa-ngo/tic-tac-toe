from player import *

class Board:

    def __init__(self, x , o):
        self._board = [None, None, None, None, None, None, None, None, None]
        self._x = x.get_player_role()
        self._o = o.get_player_role()
        self._curr_player = self._x

    def set_pos(self, index_num):
        print("Before: ", self.get_board())
        self._board[index_num] = self._curr_player
        print("After: ", self.get_board())

        if self._curr_player == self._x:
            self._curr_player = self._o
        self._curr_player = self._o
        return self.get_board()

    def get_board(self):
        return self._board

    def get_curr_player(self):
        return self._curr_player





