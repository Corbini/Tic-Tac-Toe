from PyQt6.QtWidgets import QLabel, QMainWindow
from PyQt6.QtGui import *
from graphic_map import GraphicMap
from buttons import Button, TextBox


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

