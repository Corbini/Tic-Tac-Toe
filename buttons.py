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
    def __init__(self, text, button_png):
        super(Button, self).__init__()
        self.setLayout(QVBoxLayout())
        if button_png is not None:
            self.image(button_png)
            size = button_png.size()
            self.layout().addWidget(TextBox(text, size.width(), size.height(), 30))
        pass

    def image(self, image):
        self.setFixedSize(image.size())
        self.setPixmap(image)
