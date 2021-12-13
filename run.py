# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# imports
import subprocess
import platform
from random import *
from enum import Enum


# contstants
letters_to_num = {"A": 0, "B": 1, "a": 0, "b": 1}
score_to_win = 2

letters = ["A", "B"]
if platform.system() == "Windows":
    command_to_clear = "cls"
else:
    command_to_clear = "clear"

class Turn(Enum):
    player = 0
    computer = 1

def print_hr():
    print("| ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |")

# Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Board class
class Board:
    def __init__(self, point):
        self.board = [[" "] * point.x for i in range(point.y)]  # list of rows
        self.size = point

    def print(self):
        """
        Method prints the board to console
        :return: None
        """
        print("  A B")
        row_number = 0
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


# Game class
class Game:
    def __init__(self, player_name):
        self.player_name = player_name
        self.size = Point(2, 2)

        self.player_board = Board(self.size)
        self.computer_board = Board(self.size)
        self.player_guess_board = Board(self.size)
        self.computer_guess_board = Board(self.size)


        self.player_score = 0
        self.computer_score = 0
        self.result = None #win, lose, quit

    def create_ships(self, board):
        """
        Method creates ships in the board randomly
        :return: None
        """
        for i in range(2):
            ship_row, ship_column = randint(0, 1), randint(0, 1)
            while board[ship_row][ship_column] == "X":
                ship_row, ship_column = randint(0, 1), randint(0, 1)
            board[ship_row][ship_column] = "X"

    @staticmethod
    def get_user_input():
        """
        Method gets user coordinates input
        :return: row and column
        """
        while True:
            hit_position = input(
                "Enter coordinates (row, column) or (number, alphabet): \n"
            )
            try:
                row, col = hit_position.split(",")
                row = int(row)
                col = letters_to_num[col]

                if col < 0 or col > 1 or row < 0 or row > 1:
                    print("Please enter a valid move!")

                    continue

            except:
                print("Please enter a valid move!")
                continue
            
            return row, col

    def check_ships_destroyed(self, turn):
        """
        Method checks if all ships are destroyed
        :return: boolean value
        """
        if turn == Turn.player:
            if self.player_score >= score_to_win:
                return True
            else:
                return False
        elif turn == Turn.computer:
            if self.computer_score >= score_to_win:
                return True
            else:
                return False

    def get_random_move(self):
        """
        Method gets random position to shoot for computer
        :return: row and column
        """
        while True:
            row = randint(0, 1)
            col = randint(0, 1)
            if self.computer_guess_board[row][col] == " ":
                return row, col

    def print_on_win(self):
        """
        Method prints to window an update of the boards
        :return: None
        """
        print("Player {} Ocean:".format(self.player_name))
        self.player_board.print()
        print_hr()
        print("Computer Ocean:")
        self.computer_board.print()
        print_hr()

    def start_game(self):
        """
        Method: Main game loop
        :return: None
        """
        turn = Turn.player # represents player turn
        self.create_ships(self.player_board)
        self.create_ships(self.computer_board)

        subprocess.run(command_to_clear)
        print_hr()
        
        while True:
            if turn == Turn.player:  # player's turn
                print(f"{self.player_name}'s turn:")
                print_hr()
                print(f"{self.player_name}'s Ocean:")
                self.player_board.print()
                print_hr()
                print("Computer's Board:")
                self.player_guess_board.print()

                row, col = self.get_user_input()
        
                while self.player_guess_board[row][col] != " ":
                    print("You have already shot here!")
                    row, col = self.get_user_input()

                if self.computer_board[row][col] == "X":
                    self.player_guess_board[row][col] = "X"
                    self.player_score += 1
                    print("You hit a ship!")
                else:
                    self.player_guess_board[row][col] = "O"
                    print("You missed the shot!")

                print_hr()
                print(
                    f"Current Score: {self.player_name} - {self.player_score}, Computer - {self.computer_score}"
                )

                is_win = self.check_ships_destroyed(turn)

                if not is_win:
                    input("Computer's turn now! Press Enter to continue...")
                    turn = Turn.computer
                    subprocess.run(command_to_clear)

                if is_win:
                    subprocess.run(command_to_clear)
                    self.print_on_win()
                    print("You hit the final ship!")
                    print_hr()
                    win = str(
                        self.player_name + " wins the game! Congratulations!"
                    )
                    print(win)
                    self.result = "player_win"
                    input("Press enter!")
                    break

            elif turn == Turn.computer:  # computer's turn
                subprocess.run(command_to_clear)
                print("Computer's turn: ")
                row, col = self.get_random_move()

                while self.computer_guess_board[row][col] != " ":
                    row, col = self.get_random_move()
                    if self.computer_guess_board[row][col] == " ":
                        break

                print_hr()
                print(f"Computer shot at ({row}, {letters[col]})")
                print_hr()

                if self.player_board[row][col] == "X":
                    self.computer_guess_board[row][col] = "X"
                    self.computer_score += 1
                    print("Computer hit a ship!")
                else:
                    self.computer_guess_board[row][col] = "O"
                    print("Computer missed the shot!")

                print_hr()
                print(
                    f"Current Score: {self.player_name} - {self.player_score}, Computer - {self.computer_score}"
                )
                print_hr()

                print("Computer Shots Till Now:")
                self.computer_guess_board.print()
                print_hr()

                is_win = self.check_ships_destroyed(turn)

                if not is_win:
                    while True:
                        res = input("Do you want to continue? (y/n) \n")
                        if res == "y" or res == "Y":
                            turn = Turn.player
                            subprocess.run(command_to_clear)
                            break
                        elif res == "n" or res == "N":
                            self.result = "player_quit"
                            break
                        else:
                            print("Invalid input!")
                            continue

                    if self.result == "player_quit":
                        break

                if is_win:
                    input("Press Enter to Continue...")
                    subprocess.run(command_to_clear)
                    self.print_on_win()
                    print("Computer hit your final ship!")
                    print_hr()
                    win = str(
                        "You Lose! Computer wins the game! Unlucky!"
                    )
                    print(win)
                    self.result = "player_lose"
                    input("Press enter!")
                    break


def exit_game():
    print()
    print_hr()
    print("Sad to see you go. Try again later!")
    print_hr()
    exit()

def main():
    subprocess.run(command_to_clear)

    while True:
        subprocess.run(command_to_clear)
        option = input(
            f"""
| ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |
| ~ ~ ~ ~ ~ ~ ~ ~ ~Battleship ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |
| ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |

Welcome to Battleship!
Board Size: 10 x 10, Number of Ships: {score_to_win}
Have Fun!

Choose option:
(1) Start Battleship Game
(2) Show the game rules
(3) Exit Game
"""
        )
        if option == "1":
            print_hr()
            player_name = input("Enter name of player: \n")
            print_hr()
            input("Press Enter to continue...")

            while option == "1":
                subprocess.run(command_to_clear)
                game = Game(player_name)
                game.start_game()

                if game.result == "player_quit":
                    exit_game()

                while (
                    game.result == "player_win" or game.result == "player_lose"
                ):
                    res = input("Would you like to play again? (y/n) \n")
                    if res == "y" or res == "Y":
                        print_hr()
                        print(" The game will continue!")
                        print_hr()
                        input("Press Enter to continue...")
                        break
                    elif res == "n" or res == "N":
                        exit_game()
                    else:
                        print("Invalid input! Only 'y' or 'n' are allowed.")

        elif option == "2":
            subprocess.run(command_to_clear)
            print_hr()
            print("Here are the Game Rules!")
            print_hr()

            print(
                f"""
Rules:
1. The board is 10 x 10
2. Each player has {score_to_win} ships
3. Ships are placed randomly
4. Ships cannot overlap with each other
5. Ships cannot be placed in the same position
6. Ships cannot be placed on the edge of the board
7. Players take turns firing shots (calling out grid coordinates) 
8. Grid coordinates have the following format (e.g): "1,a", "2,b", "4,e"
9. Players attempt to hit the opponent's enemy ships.
10. When a ship it "hit", it is considered sunk
11. As soon as all of one player's ships have been sunk, the game ends.
            """
            )
            print_hr()
            input("Press Enter to continue...")

        elif option == "3":
            exit_game()
                
if __name__ == "__main__":
    main()