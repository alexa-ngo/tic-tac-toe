from board import *

class Game:

    def __init__(self, the_board, p1, p2):
        self._x = p1.get_player_role()
        self._o = p2.get_player_role()
        self._the_board = the_board

    # Get at specific indices to check if there is three of the same symbol
    def check(self, board):
        print("The board: ")
        b = board

        # O wins for horizontal lines
        if (b.get_pos(0) == "o" and b.get_pos(1) == "o" and b.get_pos(2) == "o" or
                b.get_pos(3) == "o" and b.get_pos(4) == "o" and b.get_pos(5) == "o" or
                b.get_pos(6) == "o" and b.get_pos(7) == "o" and b.get_pos(8) == "o"):
            return "o wins!"

        # X wins for horizontal lines
        if (b.get_pos(0) == "x" and b.get_pos(1) == "x" and b.get_pos(2) == "x" or
                b.get_pos(3) == "x" and b.get_pos(4) == "x" and b.get_pos(5) == "x" or
                b.get_pos(6) == "x" and b.get_pos(7) == "x" and b.get_pos(8) == "x"):
            return "x wins!"

        # O wins for vertical lines
        if (b.get_pos(0) == "o" and b.get_pos(3) == "o" and b.get_pos(6) == "o" or
                b.get_pos(1) == "o" and b.get_pos(4) == "o" and b.get_pos(7) == "o" or
                b.get_pos(2) == "o" and b.get_pos(5) == "o" and b.get_pos(8) == "o"):
            return "o wins!"

        # X wins for vertical lines
        if (b.get_pos(0) == "x" and b.get_pos(3) == "x" and b.get_pos(6) == "x" or
                b.get_pos(1) == "x" and b.get_pos(4) == "x" and b.get_pos(7) == "x" or
                b.get_pos(2) == "x" and b.get_pos(5) == "x" and b.get_pos(8) == "x"):
            return "x wins!"

        # O wins for diagonals
        if (b.get_pos(0) == "o" and b.get_pos(4) == "o" and b.get_pos(8) == "o" or
                b.get_pos(2) == "o" and b.get_pos(4) == "o" and b.get_pos(6) == "o"):
            return "o wins!"

        # X wins for diagonals
        if (b.get_pos(0) == "x" and b.get_pos(4) == "x" and b.get_pos(8) == "x" or
                b.get_pos(2) == "x" and b.get_pos(4) == "x" and b.get_pos(6) == "x"):
            return "x wins!"


    def get_board(self):
        return self._the_board

    def is_game_over(self, board):
        if self.check(board) == "x wins!" or self.check(board) == "o wins!":
            print("The game is over!")
            return

    def is_tied(self, board):
        print("Here is the value of board", self.check(board))
        if self.check(board) == "x wins!" or self.check(board) == "o wins!":
            return
        print("Here is the board: ", self.get_board())
        # elif len(self.get_board()) == 9:
        #     print("The current board length is: ", len(board))
        #     return "There is a tie!"





