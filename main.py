

class Map:
    def __init__(self):
        self.structure= [[0 for x in range(3)] for y in range(3)]
        # 0 is empty, 1 is X, 2 is O

    def mark_place(self, place):
        # Checking if place is empty

        print(place[0])
        print(place[1])

        return True

    def check_for(self, player):
        #win check for player

        return False

    def is_full(self):
        #check for new move

        return False

    def check_result(self):
        # find if game ended

        x_player_win = False
        y_player_win = False
        draw = False

        return False

    def show_in_terminal(self):
        # print in terminal

        pass


class Window:
    def __init__(self):
        # Create window handle

        pass

    def game_window(self, game_map):
        # Create game stage

        pass

    def start_window(self):
        # Create start stage

        pass

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

    row = 1
    column = 2

    return row, column


def get_computer_mark():
    # randomize computer input

    row = 0
    column = 1

    return row, column


def main():
    print("Hello")
    game_map = Map()
    game_map.show_in_terminal()
    game_map.mark_place(get_player_mark())


main()
