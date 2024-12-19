from player import *

class Board:

    def __init__(self, player1 , player2):
        self._board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self._x = player1.get_player_role()
        self._o = player2.get_player_role()
        self._curr_player = self._x

    # Iterates through each cell of the board
    def __iter__(self):
        self.current_board_idx = 0
        self.board_to_iterate = list(self._board)
        return self

    def __next__(self):
        if self.current_board_idx < len(self.board_to_iterate):
            curr_result = self.board_to_iterate[self.current_board_idx]
            self.current_board_idx += 1
            return curr_result

        raise StopIteration

    def clear_board(self):
        self._board = [" "] * 9

    def get_board(self):
        return self._board

    def get_curr_player(self):
        return self._curr_player

    def get_pos(self, index_num):
        return self._board[index_num]

    def set_pos(self, index_num):

        index_num = int(index_num)
        # Check to see if the index number is within the range and valid
        self.is_valid(int(index_num))

        if self._board[index_num] != " ":
            raise TypeError("Sorry, this index is occupied. Please choose another index.")

        self._board[index_num] = self._curr_player

        # Switch roles after the position Player X has taken their turn
        if self._curr_player == self._x:
            self._curr_player = self._o

        return

    # will implement a check to see if there is a tie if the board is full


    def is_valid(self, index_num):
        """
        Checks to see if the index is within the range of the board
        """

        if index_num < 0 or index_num > 8:
            raise IndexError("Sorry, index out of range.")

    def print_board(self):
        idx = 0
        for cell in self._board:
            print(f"{idx}: {cell}")
            idx += 1
        return

    def print_formatted_board(self):
        b = self._board
        print("\n")
        print(f" {b[0]} | {b[1]} | {b[2]} ")
        print(f" ----------")
        print(f" {b[3]} | {b[4]} | {b[5]} ")
        print(f" ----------")
        print(f" {b[6]} | {b[7]} | {b[8]} ")
        print("\n")

    def new_round(self):
        """
        Sets the first player back to Player X after every round.
        """
        self._curr_player = self._x

    def start_game(self):
        player1 = Player("x")
        player2 = Player("o")

        board = Board(player1, player2)
        return board



