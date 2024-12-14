class Board:

    def __init__(self, player1 , player2):
        self._board = [None, None, None, None, None, None, None, None, None]
        self._x = player1.get_player_role()
        self._o = player2.get_player_role()
        self._curr_player = self._x

    # Implemented an iterator of the board to give people the flexibility
    # to iterate through each cell
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
        self._board = [None] * 9

    def get_curr_player(self):
        return self._curr_player

    def get_pos(self, index_num):
        return self._board[index_num]

    def set_pos(self, index_num):
        self.is_valid(index_num)

        self._board[index_num] = self._curr_player

        if self._curr_player == self._x:
            self._curr_player = self._o
        return

    # check if it is a tie if the board is full

    def is_valid(self, index_num):
        if index_num < 0 or index_num > 8:
            raise IndexError("Sorry, index out of range.")

    def iterate_through_board(self):
        idx = 0
        for cell in self._board:
            print(f"{idx}: {cell}")
            idx += 1

    def new_round(self):
        self._curr_player = self._x



