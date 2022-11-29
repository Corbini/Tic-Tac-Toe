from PyQt6.QtWidgets import QLabel, QMainWindow
from PyQt6.QtGui import *
from graphic_map import GraphicMap, Results
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

    def game_window(self, action=None):
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
        self.map = GraphicMap(self.layout(), self.end_window)

    def clear(self):
        children = self.children()
        for child in children[2:]:
            child.deleteLater()

    def add_text(self, text, x, y, width, height, font_size=32):
        text = TextBox(text, width, height, font_size)
        text.move(x, y)
        self.layout().addWidget(text)

    def add_button(self, button_png, text, func, x, y):
        button = Button(text, button_png)
        button.mousePressEvent = func
        button.move(x, y)
        self.layout().addWidget(button)

    def start_window(self, action=None):
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

        # get Result
        text = ""
        match self.map.result:
            case Results.draw:
                text = "Draw"
            case Results.X_won:
                text = "Victory"
            case Results.O_won:
                text = "Defeat"

        # Create Result Screen
        result_screen = QPixmap('images/Result_Window.png')
        self.add_button(result_screen, "", None, 353, 276)
        self.add_text(text, 353, 276, 545, 130, 96)

        # Add button
        result_options = QPixmap("images/Result_Options.png")
        self.add_button(result_options, "Another round", self.game_window, 368, 406)
        self.add_button(result_options, "to menu", self.start_window, 633, 406)

        pass

