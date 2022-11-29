# cpu input
import random


random.seed()


def get_computer_mark():
    # randomize computer input

    row = random.randint(0, 2)
    column = random.randint(0, 2)

    return row, column
