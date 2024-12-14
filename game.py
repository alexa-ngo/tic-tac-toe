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
        top_row = b.get_pos(0) and b.get_pos(1) and b.get_pos(2)
        mid_row = b.get_pos(3) and b.get_pos(4) and b.get_pos(5)
        last_row = b.get_pos(6) and b.get_pos(7) and b.get_pos(8)
        diagonal_down = b.get_pos(0) and b.get_pos(4) and b.get_pos(8)
        diagonal_up = b.get_pos(2) and b.get_pos(4) and b.get_pos(6)
        if diagonal_down == "o" or diagonal_up == "o":
            return "o wins!"
        if top_row == "x" or mid_row == "x" or last_row == "x":
            return "x wins!"
        elif top_row == "o" or mid_row == "o" or last_row == "o" or diagonal_down == "o":
            return "o wins!"
