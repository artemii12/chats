from variables import *
from main import message


def exept_hook(cls, exeption, traceback):
    sys.__excepthook__(cls, exeption, traceback)


if __name__ == '__main__':
    app, window = QApplication(sys.argv), message()
    window.show()
    sys.excepthook = exept_hook
    sys.exit(app.exec())
