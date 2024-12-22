from board import Board
from game import Game
from player import *

def start_game():
    
    print("Type in the index where you want to place either an 'x' or an 'o'. \nPlayer X will be going first and then Player Y will go next.")
    print("The first row is numbered with indices 0, 1, 2. \nThe second row is indices 3, 4, 5. \nThe last row is index 6, 7, 8.\n")
    
    player1 = Player("x")
    player2 = Player("o")
    the_board = Board(player1, player2)
    the_game = Game(the_board, player1, player2)

    game_is_active = True
    curr_player = "x"

    while game_is_active is True:
        pos_of_x_or_o = input(f"Player {curr_player}, position of {curr_player}: ")
        switch_players_or_not = the_board.set_pos(curr_player,pos_of_x_or_o)
        the_board.print_formatted_board()

        # Check if there are three symbols in a row
        results = the_game.check(the_board)
        if results == 1 or results == 0 or the_board.is_tie() is True:
            break

        result_of_out_of_range = the_board.is_valid(int(pos_of_x_or_o))

        if switch_players_or_not is False or result_of_out_of_range is False:
            curr_player = curr_player
        else:
            if "x" == curr_player:
                curr_player = "o"
            else:
                curr_player = "x"

    else:
        print("Sorry to see you go! See you next time!")

    # Check if there are three symbols in a row
    results = the_game.check(the_board)

    if results is None:
        print("There is a tie!")

    if results == 1 or results == 0:
        print(f"Yeah! {curr_player} got three in a row!")

    print("Thanks for playing!")

    # Ask the player if they want to play again
    print("------------------ ")
    play_again_response = input("Would you like to play again? (Y/N)\n\n").upper()
    if play_again_response == "Y":
        start_game()
    else:
        print("Goodbye!\n")

start_game()