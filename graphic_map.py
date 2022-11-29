from PyQt6.QtGui import *
from map import Map, Players, Results
from cpu import get_computer_mark
from functools import partial
from buttons import Button


class GraphicMap:
    def __init__(self, screen, ending):

        self.map = Map()
        self.screen = screen
        self.ending = ending
        self.result = Results.running

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
        button = Button("", None)
        button.mousePressEvent = partial(self.interact, button, map_coord, Players.X)
        button.move(column, row)
        self.buttons[map_coord[0]][map_coord[1]] = button
        pass

    def update(self):
        self.result = self.map.check_result()

        if self.result is not Results.running:
            self.ending()

    def interact(self, button, map_coord, player, event):
        if self.map.mark_place(map_coord, player):
            button.image(self.player_x)

            self.update()

            if self.result == Results.running:
                self.cpu_interact()

    def cpu_interact(self):
        # get move
        cpu_move = get_computer_mark()
        while not self.map.mark_place(cpu_move, Players.O):
            cpu_move = get_computer_mark()

        # print move
        self.buttons[cpu_move[0]][cpu_move[1]].image(self.player_o)

        self.update()
