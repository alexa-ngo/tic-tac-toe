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
            print("6")
            return "o wins!"

        # X wins for horizontal lines
        if (b.get_pos(0) == "x" and b.get_pos(1) == "x" and b.get_pos(2) == "x" or
                b.get_pos(3) == "x" and b.get_pos(4) == "x" and b.get_pos(5) == "x" or
                b.get_pos(6) == "x" and b.get_pos(7) == "x" and b.get_pos(8) == "x"):
            print("7")
            return "x wins!"

        # O wins for vertical lines
        if (b.get_pos(0) == "o" and b.get_pos(3) == "o" and b.get_pos(6) == "o" or
                b.get_pos(1) == "o" and b.get_pos(4) == "o" and b.get_pos(7) == "o" or
                b.get_pos(2) == "o" and b.get_pos(5) == "o" and b.get_pos(8) == "o"):
            print("8")
            return "o wins!"

        # X wins for vertical lines
        if (b.get_pos(0) == "x" and b.get_pos(3) == "x" and b.get_pos(6) == "x" or
                b.get_pos(1) == "x" and b.get_pos(4) == "x" and b.get_pos(7) == "x" or
                b.get_pos(2) == "x" and b.get_pos(5) == "x" and b.get_pos(8) == "x"):
            print("9")
            return "x wins!"

        # O wins for diagonals
        if (b.get_pos(0) == "o" and b.get_pos(4) == "o" and b.get_pos(8) == "o" or
                b.get_pos(2) == "o" and b.get_pos(4) == "o" and b.get_pos(6) == "o"):
            print("10")
            return "o wins!"

        # X wins for diagonals
        if (b.get_pos(0) == "x" and b.get_pos(4) == "x" and b.get_pos(8) == "x" or
                b.get_pos(2) == "x" and b.get_pos(4) == "x" and b.get_pos(6) == "x"):
            print("10")
            return "x wins!"
