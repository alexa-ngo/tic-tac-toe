from board import Board
from game import Game
from player import *

def start_game():

    response = input("Would you like to play tic-tac-toe? (Yes/No) ")

    player1 = Player("x")
    player2 = Player("o")
    the_board = Board(player1, player2)
    the_game = Game(the_board, player1, player2)

    game_is_active = True

    curr_player = "X"

    if response == "Yes":
        while game_is_active is True:
            pos_of_x_or_o = input(f"Player {curr_player}, position of {curr_player}: ")
            print("Here is the pos_of_x_or_o: ", curr_player, "and its position: ", pos_of_x_or_o)
            the_board.set_pos(pos_of_x_or_o)
            the_board.print_formatted_board()
            # # Check if there are three symbols in a row
            # results = the_game.check(the_board)
            # if results == "x wins!" or results == "o wins!":
            #     print(f"Yeah! {curr_player} got three in a row!")
            #     game_is_active = False
            #     break
            # the_game.is_tied(the_board)
            # # resets the player to be x
            # #the_board.new_round()
            if "X" == curr_player:
                curr_player = "O"
            else:
                curr_player = "X"
    else:
        print("Sorry to see you go! See you next time!")

    print("Thanks for playing!")

    # Ask the player if they want to play again



    #     pos_of_x = input("Player 1, position of X? ")
    #     the_board.set_pos(pos_of_x)
    #     the_board.print_formatted_board()
    #     pos_of_y = input("Player 2, position of O? ")
    #     the_board.set_pos(pos_of_y)
    #     the_board.print_formatted_board()
    #     the_board.new_round()
    #
    #     print("Nice! Let's keep playing!")
    #     pos_of_x = input("Player 1, position of X? ")
    #     the_board.set_pos(pos_of_x)
    #     the_game.check(the_board)
    #
    #     the_board.print_formatted_board()
    #     pos_of_y = input("Player 2, position of O? ")
    #     the_board.set_pos(pos_of_y)
    #     the_game.check(the_board)
    #
    #     the_board.print_formatted_board()
    #     the_board.new_round()
    #
    #
    #     ## Make a flag
    #
    #     # while the flag is xxxx:
    #     # keep running this:
    #
    #     print("Hi1")
    #
    #     pos_of_x = input("Player 1, position of X? ")
    #     the_board.set_pos(pos_of_x)
    #     the_game.check(the_board)
    #
    #     the_board.print_formatted_board()
    #     the_game.is_game_over(the_board)
    #
    #     the_game.is_tied(the_board)
    #
    #     the_board.new_round()
    #
    #     print("Bye1")
    #
    #     pos_of_y = input("Player 2, position of O? ")
    #     the_board.set_pos(pos_of_y)
    #     the_game.check(the_board)
    #
    #     the_board.print_formatted_board()
    #
    #     the_game.is_game_over(the_board)
    #
    #     the_game.is_tied(the_board)
    #
    #
    #     the_board.new_round()
    #
    #     print("Hi2")
    #
    #     pos_of_x = input("Player 1, position of X? ")
    #     the_board.set_pos(pos_of_x)
    #     the_game.check(the_board)
    #     the_game.is_game_over(the_board)
    #
    #     the_game.is_tied(the_board)
    #
    #     the_board.print_formatted_board()
    #     the_board.new_round()
    #
    #     print("Bye2")
    #
    #     pos_of_y = input("Player 2, position of O? ")
    #     the_board.set_pos(pos_of_y)
    #     the_game.check(the_board)
    #     the_game.is_game_over(the_board)
    #
    #     the_game.is_tied(the_board)
    #
    #     the_board.print_formatted_board()
    #     the_board.new_round()
    #
    #     print("Hi3")
    #
    #     pos_of_x = input("Player 1, position of X? ")
    #     the_board.set_pos(pos_of_x)
    #     the_game.check(the_board)
    #     the_game.is_game_over(the_board)
    #
    #     the_game.is_tied(the_board)
    #
    #     the_board.print_formatted_board()
    #     the_board.new_round()
    #
    #     print("Bye3")
    #
    #     pos_of_y = input("Player 2, position of O? ")
    #     the_board.set_pos(pos_of_y)
    #     the_game.check(the_board)
    #     the_game.is_game_over(the_board)
    #
    #     the_game.is_tied(the_board)
    #
    #     the_board.print_formatted_board()
    #
    #     print("Bye-bye!")
    # else:
    #     print("Sorry to see you go! Lets play next time!")


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