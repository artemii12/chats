import sys
from PyQt6.QtWidgets import QApplication
from main import main

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main.instance()
    window.show()
    app.exec()