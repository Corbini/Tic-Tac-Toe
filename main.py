from enum import Enum
import re
import random


class Players(Enum):
    X = 1
    O = 2


class Results(Enum):
    running = 0
    X_won = 1
    draw = 2
    O_won = 3


class Map:
    def __init__(self):
        self.structure = [[0 for x in range(3)] for y in range(3)]
        # 0 is empty, 1 is X, 2 is O

    def mark_place(self, place, player: Players):
        # Checking if place is empty

        if self.structure[place[0]][place[1]] == 0:
            self.structure[place[0]][place[1]] = player.value
            return True

        return False

    def check_for(self, player: Players):
        # win check for player

        # line up-down
        for column in range(0, 2):
            flag = True
            for row in range(0, 2):
                if self.structure[column][row] != player.value:
                    flag = False
                    break
            if flag is True:
                return True

        # line left-right
        for row in range(0, 2):
            flag = True
            for column in range(0, 2):
                if self.structure[column][row] != player.value:
                    flag = False
                    break
            if flag is True:
                return True

        # crosses
        flag = True
        for diagonal in range(0, 2):
            if self.structure[diagonal][diagonal] != player.value:
                flag = False
                break
        if flag is True:
            return True

        flag = True
        for diagonal in range(0, 2):
            if self.structure[diagonal][2 - diagonal] != player.value:
                flag = False
                break
        if flag is True:
            return True

        return False

    def is_full(self):
        # check for new move

        for row in self.structure:
            for space in row:
                if space == 0:
                    return False

        return True

    def check_result(self):
        # find if game ended

        if self.check_for(Players.X):
            return Results.X_won

        if self.check_for(Players.O):
            return Results.O_won

        if self.is_full():
            return Results.draw

        return Results.running

    def show_in_terminal(self):
        # print in terminal

        text = "map:\n"

        for row in self.structure:
            for space in row:
                if space == 1:
                    text += "X "

                elif space == 2:
                    text += "O "
                else:
                    text += "_ "
            text += "\n"

        print(text)


class Window:
    def __init__(self):
        # Create window handle

        pass

    def game_window(self, game_map):
        # Create game stage

        pass

    def start_window(self):
        # Create start stage

        pass

    def end_window(self):
        # Create end stage

        pass

    def refresh(self):
        # Update graphic

        pass

    def get_player_input(self):
        # Get user mouse input
        pass


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


def get_computer_mark():
    # randomize computer input

    row = random.randint(0, 2)
    column = random.randint(0, 2)

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


def main():
    print("Hello")

    terminal_game_mode()


random.seed()
main()
