
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QPushButton, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QRegion
from PyQt6.QtCore import Qt, QSize


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
