# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#imports
import os
from random import *

#contstants
let_to_num = {
    "A": 0,
    "B": 1,
}

lets = ["A", "B"]
command_to_clear = "clear"

def print_hr():
    print("| ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  |")

# Game class
class Game:
    def __init__(self, player_name):
        pass

    def print_board(self, board):
        pass

    def create_ships(self, board):
        pass

    def check_ships_destroyed(self, turn):
        pass

    def get_random_move(self):
        pass

    def print_on_win(self):
        pass

    def start_game(self):
        pass


def exit_game():

def main():
    
    os.system(command_to_clear)

    while True:
        os.system(command_to_clear)
        option = input(
            """
| ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  |
| ~ ~ ~ ~ ~ ~ ~ ~ ~Battleship ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  |
| ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  |

Welcome to Battleship!
Board Size: 10 x 10, Number of Ships: 5
Have Fun!

Choose option:
(1) Start Battleship Game
(2) Show the game rules
(3) Exit Game
"""
        )
        if option == "1":
            print_hr()
            player_name = input("Enter name of player: ")
            print_hr()
            input("Press Enter to continue...")

            while option == "1":
                os.system(command_to_clear)
                game = Game(player_name)
                game.start_game()

                if game.result == "player_quit":
                    exit_game()

                while (
                    game.result == "player_win" or game.result == "player_lose"
                ):
                    res = input("Would you like to play again? (y/n) ")
                    if res == "y":
                        print_hr()
                        print(" The game will continue!")
                        print_hr()
                        input("Press Enter to continue...")
                        break
                    elif res == "n":
                        exit_game()
                    else:
                        print("Invalid input! Only 'y' or 'n' are allowed.")

        elif option == "2":
            os.system(command_to_clear)
            print_hr()
            print("Here are the Game Rules!")
            print_hr()

            print(
                """
Rules:
1. The board is 10 x 10
2. Each player has 5 ships
3. Ships are placed randomly
4. Ships cannot overlap with each other
5. Ships cannot be placed in the same position
6. Ships cannot be placed on the edge of the board
            """
            )

            print_hr()
            input("Press Enter to continue...")

        elif option == "3":
            exit_game()

                
if __name__ == "__main__":
    main()