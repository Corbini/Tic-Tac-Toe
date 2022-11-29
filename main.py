from window import Window
from terminal import terminal_game_mode
from PyQt6.QtWidgets import QApplication
import sys


def main():
    print("Hello")

    app = QApplication(sys.argv)
    game = Window(app)
    app.exec()
    # terminal_game_mode()


main()
