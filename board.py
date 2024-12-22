from player import *

class Board:

    def __init__(self, player1 , player2):
        self._board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self._x = player1.get_player_role()
        self._o = player2.get_player_role()
        self._curr_player = self._x

    def __iter__(self):
        """
        Iterates through each cell of the board
        """
        self.current_board_idx = 0
        self.board_to_iterate = list(self._board)
        return

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

    def set_pos(self, curr_player, index_num=0):
        """
        Set the position based on the index number
        """

        # Convert the string index_num into an int
        index_num = int(index_num)

        # Ask the player for another position if their index_num is out of range
        if len(self._board) < index_num:
            self.start_game()
            return False

        # Check the index number is within the range
        # Redo turn when the space is occupied
        if self._board[index_num] != " " or self.is_valid(index_num) is False:
            self.start_game()
            print("Sorry, this index is occupied. Please choose another index.")
            return False

        else:
            self._board[index_num] = curr_player
            return

    def is_tie(self):

        count = 0
        for each in self._board:
            if each != " ":
                count = count + 1

        # Returns True if there is a tie
        if count == 9:
            return True

    def is_valid(self, index_num):
        """
        Checks to see if the index is within the range of the board
        """
        if index_num < 0 or index_num > 8:
            print("Sorry, index of of range.")
            return False

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

    def start_game(self):
        player1 = Player("x")
        player2 = Player("o")

        board = Board(player1, player2)
        return board



