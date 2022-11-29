
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QPushButton, QVBoxLayout, QGridLayout
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from map import Map, Players, Results
from cpu import get_computer_mark
from functools import partial


class TextBox(QLabel):
    def __init__(self, text, x, y):
        super(TextBox, self).__init__(text)
        self.setFont(QFont('Julee', 32))
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedSize(x, y)


class Button(QLabel):
    def __init__(self, text):
        super(Button, self).__init__()
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(TextBox(text, 300, 100))
        pass

    def image(self, image):
        self.setFixedSize(image.size())
        self.setPixmap(image)


class GraphicMap:
    def __init__(self, screen, ending):

        self.map = Map()
        self.screen = screen
        self.ending = ending

        self.buttons = [[0 for x in range(3)] for y in range(3)]
        self.player_x = QPixmap('images/X_Player.png')
        self.player_o = QPixmap('images/O_Player.png')

        self.gen_map()

    def gen_map(self):
        self.add_button(159, 139, 302, 252, [0, 0])
        self.add_button(461, 139, 315, 252, [0, 1])
        self.add_button(776, 139, 376, 252, [0, 2])
        self.add_button(159, 391, 311, 247, [1, 0])
        self.add_button(470, 391, 306, 247, [1, 1])
        self.add_button(776, 391, 376, 247, [1, 2])
        self.add_button(159, 638, 317, 300, [2, 0])
        self.add_button(476, 638, 314, 300, [2, 1])
        self.add_button(790, 638, 362, 300, [2, 2])

        for button_row in self.buttons:
            for button in button_row:
                self.screen.addWidget(button)

    def add_button(self, column, row, width, high, map_coord):
        button = Button("")
        button.mousePressEvent = partial(self.interact, button, map_coord, Players.X)
        button.move(column, row)
        self.buttons[map_coord[0]][map_coord[1]] = button
        pass

    def interact(self, button, map_coord, player, event):

        if self.map.mark_place(map_coord, player):
            button.image(self.player_x)

        if self.map.check_result() is not Results.running:
            self.ending()

        # self.cpu_interact()

    def cpu_interact(self):
        cpu_move = get_computer_mark()
        while self.map.mark_place(cpu_move, Players.O):
            cpu_move = get_computer_mark()

        self.buttons[cpu_move[0]][cpu_move[1]].image(self.player_o)

        if self.map.check_result() is not Results.running:
            self.ending()


class Window(QMainWindow):
    def __init__(self, qapp):
        # pyqt6 init
        self.app = qapp
        super().__init__()

        # window setup
        self.setWindowTitle("Tic Tac Toe")
        self.setWindowIcon(QIcon('images/Logo.png'))
        self.setFixedSize(1280, 960)
        self.background = QLabel()
        self.setCentralWidget(self.background)
        self.show()

        # Starting mode
        self.start_window()

    def game_window(self, game_map):
        # Create game stage
        self.clear()

        # Load Images
        game_window_png = QPixmap('images/Game_Window.png')

        # Set Background
        self.background.setPixmap(game_window_png)

        # Set scoreboard
        self.add_text("Player", 79, 22, 400, 100)
        self.add_text("Cpu", 751, 22, 400, 100)

        # Gen map
        GraphicMap(self.layout(), self.end_window)

    def clear(self):
        children = self.children()
        for child in children[2:]:
            child.deleteLater()

    def add_text(self, text, x, y, width, height):
        text = TextBox(text, width, height)
        text.move(x, y)
        self.layout().addWidget(text)

    def add_button(self, button_png, text, func, x, y):
        button = Button(text)
        button.image(button_png)
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
        self.clear()
        # Create end stage

        pass

