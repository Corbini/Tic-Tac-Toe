from enum import Enum


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
