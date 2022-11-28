from map import *
from window import *
from terminal import *



def main():
    print("Hello")

    app = QApplication(sys.argv)
    game = Window(app)
    app.exec()


random.seed()
main()
