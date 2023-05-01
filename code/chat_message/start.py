from variables import *
from main import instance


def exept_hook(cls, exeption, traceback):
    sys.__excepthook__(cls, exeption, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = instance()
    window.show()
    sys.excepthook = exept_hook
    sys.exit(app.exec())
