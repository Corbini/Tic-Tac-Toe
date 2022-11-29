from PyQt6.QtCore import *
from PyQt6.QtWidgets import QLabel, QVBoxLayout
from PyQt6.QtGui import *


class TextBox(QLabel):
    def __init__(self, text, x, y, font_size):
        super(TextBox, self).__init__(text)
        self.setFont(QFont('Julee', font_size))
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedSize(x, y)


class Button(QLabel):
    def __init__(self, text):
        super(Button, self).__init__()
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(TextBox(text, 300, 100, 32))
        pass

    def image(self, image):
        self.setFixedSize(image.size())
        self.setPixmap(image)
