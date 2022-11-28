from map import *
from cpu import *

# terminal input check
import re


def get_player_mark():
    # get console input

    column = input("Please Enter column number (1-3): ")
    while not re.match("^[1-3]$", column):
        print("Incorrect input.")
        column = input("Please Enter column number (1-3): ")

    row = input("Please Enter row number (1-3): ")
    while not re.match("^[1-3]$", row):
        print("Incorrect input.")
        row = input("Please Enter row number (1-3): ")

    row = int(row) - 1
    column = int(column) - 1

    return row, column


def terminal_game_mode():
    # Map init
    game_map = Map()
    results = game_map.check_result()

    # Game Loop
    while results is results.running:
        # Show map
        game_map.show_in_terminal()

        # Player move
        while not game_map.mark_place(get_player_mark(), Players.X):
            print("Space is occupied")

        results = game_map.check_result()
        if results is Results.X_won:
            break

        # Computer move
        while not game_map.mark_place(get_computer_mark(), Players.O):
            pass

        game_map.check_result()

    # End Screen
    game_map.show_in_terminal()

    if results is Results.X_won:
        print("Congratulation! You win")

    if results is Results.draw:
        print("Draw")

    if results is Results.O_won:
        print("Oh no. Computer won. You can do it")
