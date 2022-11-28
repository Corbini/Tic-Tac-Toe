from enum import Enum

# terminal input check
import re

# cpu input
import random

# window lib
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QPushButton, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QRegion
from PyQt6.QtCore import Qt, QSize


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


class Button(QLabel):
    def __init__(self, image, text):
        super(Button, self).__init__()
        self.setFixedSize(image.size())
        self.setPixmap(image)
        pass


class Window(QMainWindow):
    def __init__(self, qapp):
        self.app = qapp
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setWindowIcon(QIcon('images/Logo.png'))
        self.background = QLabel()
        self.setCentralWidget(self.background)
        self.grid = QGridLayout()
        self.background.setLayout(self.grid)
        self.show()
        self.start_window()

    def game_window(self, game_map):
        # Create game stage
        self.clear()

        # Load Images
        game_window_png = QPixmap('images/Game_Window.png')

        # Set Background
        background = QLabel(self)
        background.setPixmap(game_window_png)
        self.setCentralWidget(background)

        pass

    def clear(self):
        children = self.children()
        for child in children[2:]:
            child.deleteLater()

    def add_button(self, button_png, text, func, x, y):
        button = Button(button_png, text)
        button.mousePressEvent = func
        button.move(x, y)
        self.layout().addWidget(button)

    def start_window(self):
        # Clearing window
        self.clear()

        # Create start stage
        menu_window_png = QPixmap('images/Menu_Window.png')
        button_png = QPixmap('images/Button.png')

        # Adding background
        self.background.setPixmap(menu_window_png)

        # Adding start button
        self.add_button(button_png, "Start Game", self.game_window, 490, 580)

        # Adding quit button
        self.add_button(button_png, "Quit", self.close, 490, 770)

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

    app = QApplication(sys.argv)
    game = Window(app)
    app.exec()


random.seed()
main()
