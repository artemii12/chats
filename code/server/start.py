from varibles import *
from main import Server
def exept_hook(cls, exeption, traceback):
    sys.__excepthook__(cls, exeption, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Server()
    window.setObjectName("MainWindow")
    window.setStyleSheet(qdarktheme.load_stylesheet(custom_colors={'foreground>input.placeholder': '#D0BCFF',
                                                                   "primary": "#D0BCFF",
                                                                   'border': '#202124'}))
    window.show()
    sys.excepthook = exept_hook
    sys.exit(app.exec())