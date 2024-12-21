from board import Board
from game import Game
from player import *

def start_game():

    response = input("Would you like to play tic-tac-toe? (Y/N) ")

    player1 = Player("x")
    player2 = Player("o")
    the_board = Board(player1, player2)
    the_game = Game(the_board, player1, player2)

    game_is_active = True

    curr_player = "x"

    if response == "Y":
        while game_is_active is True:
            pos_of_x_or_o = input(f"Player {curr_player}, position of {curr_player}: ")
            switch_players_or_not = the_board.set_pos(pos_of_x_or_o, curr_player)
            the_board.print_formatted_board()

            # Check if there are three symbols in a row
            results = the_game.check(the_board)
            if results == "x wins!" or results == "o wins!":
                print(f"Yeah! {curr_player} got three in a row!")
                game_is_active = False
                break
            # the_game.is_tied(the_board)
            # # resets the player to be x
            # #the_board.new_round()

            if switch_players_or_not == "Don't switch players":
                curr_player = curr_player
            else:
                if "x" == curr_player:
                    curr_player = "o"
                else:
                    curr_player = "x"

    else:
        print("Sorry to see you go! See you next time!")

    print("Thanks for playing!")

    # Ask the player if they want to play again
    print("------------------ ")
    play_again_response = input("Would you like to play again? (Y/N)\n")
    if play_again_response == "Y":
        start_game()
    else:
        print("Goodbye!")


#     # The X will win!
#     the_board.set_pos(0)
#     the_board.set_pos(1)
#     the_board.new_round()
#     the_board.set_pos(2)
#     the_board.set_pos(3)
#     the_board.new_round()
#     the_board.set_pos(4)
#     the_board.set_pos(5)
#     the_board.new_round()
#     the_board.set_pos(8)
#     the_board.set_pos(6)
#     the_board.set_pos(7)
#
#     # the_board.set_pos()
#     # the_board.set_pos()
#     # the_board.new_round()
#     # TEMPLATEEEEEEEEEEEEE
#     # the_board.set_pos()
#     # the_board.set_pos()
#     # the_board.new_round()
#     # the_board.set_pos()
#     # the_board.set_pos()
#     # the_board.new_round()
#     # the_board.set_pos()
#     # the_board.set_pos()
#
# # THERE WILL BE A TIE!!!!!!
# # the_board.set_pos()
# # the_board.set_pos()
# # the_board.new_round()
# # the_board.set_pos()
# # the_board.set_pos()
# # the_board.new_round()
# # the_board.set_pos()
# # the_board.set_pos()
# # the_board.new_round()
# # the_board.set_pos()
# # the_board.set_pos()
#
# # THE "X" will WIN!!!!!!!!
# # the_board.set_pos(4)
# # the_board.set_pos(0)
# # the_board.new_round()
# # the_board.set_pos(6)
# # the_board.set_pos(2)
# # the_board.new_round()
# # the_board.set_pos(7)
# # the_board.set_pos(3)
# # the_board.new_round()
# # the_board.set_pos(8)
# # the_board.set_pos(5)
#
# # THE "O" will WIN!!!!!!!!
# # the_board.set_pos(1)
# # the_board.set_pos(0)
# # the_board.new_round()
# # the_board.set_pos(2)
# # the_board.set_pos(3)
# # the_board.new_round()
# # the_board.set_pos(4)
# # the_board.set_pos(5)
# # the_board.new_round()
# # the_board.set_pos(8)
# # the_board.set_pos(6)
#
#     the_board.print_board()
#
#     alexa_game = Game(the_board, player1, player2)
#
#     # Check if there is three in a row
#     print(alexa_game.check(the_board))
#
#     # Check if there is a tie
#     print(alexa_game.is_tied())

start_game()