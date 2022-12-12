import socket
import sys
import threading
import qdarktheme
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, \
    QLabel, QLineEdit, QWidget, QCheckBox
from PyQt6 import QtGui, QtCore
#  192.168.3.4
#  25525
IPServer = ''
AddressServer = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IPServer, AddressServer))
client = []  # Массив где храним адреса клиентов
groups = []
password = {"darling": "1234"}
start = False
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.exit = True
        self.old_pos = None
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)


    def initUI(self):
        self.setGeometry(300, 300, 150, 150)
        self.setWindowTitle('Server_Window')
        self.setStyleSheet(qdarktheme.load_stylesheet(custom_colors={"primary": "#D0BCFF"}))

        self.btn = QPushButton('update', self)
        self.btn.resize(150, 20)
        self.btn.move(0, 50)
        self.btn.clicked.connect(self.update)

        self.btn = QPushButton('start_server', self)
        self.btn.resize(150, 20)
        self.btn.move(0, 75)
        self.btn.clicked.connect(self.starting_server)

        self.lbl = QLabel(self)
        self.lbl.setText('ip')
        self.lbl.move(0, -5)

        self.lbl = QLabel(self)
        self.lbl.setText('address')
        self.lbl.move(0, 20)

        self.IP_box = QLineEdit(self)
        self.IP_box.resize(100, 20)
        self.IP_box.move(50, 0)

        self.Address_box = QLineEdit(self)
        self.Address_box.resize(100, 20)
        self.Address_box.move(50, 25)


        self.Exit_menu = QPushButton('exit from settings', self)
        self.Exit_menu.resize(150, 20)
        self.Exit_menu.move(0, 100)
        self.Exit_menu.clicked.connect(self.exit_menu)

        self.all_exit = QPushButton('exit', self)
        self.all_exit.resize(150, 20)
        self.all_exit.move(0, 125)
        self.all_exit.clicked.connect(self.all_exit_program)

    def all_exit_program(self):
        del Example

    def exit_menu(self):
        Example.hide(self)

    def update(self):
        global IPServer, AddressServer, sock, start
        IPServer = str(self.IP_box.text())
        AddressServer = int(self.Address_box.text())
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.bind((str(self.IP_box.text()),
                   int(self.Address_box.text())))

        start = True

    # вызывается при нажатии кнопки мыши
    def mousePressEvent(self, event):
            if event.button() == QtCore.Qt.MouseButton.LeftButton:
                self.old_pos = event.pos()

    # вызывается при отпускании кнопки мыши
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.old_pos = None

    # вызывается всякий раз, когда мышь перемещается
    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)

    def starting_server(self):
        global start
        if start:
            t1 = threading.Thread(target=server_windows)
            t1.start()
            print('\033[40mStart Server')
            print('enabling the server\n')
            start = False
        else:
            print("обновите IpAddress")

def server_windows():
    global sock, client, groups, sock
    global start
    if start:
        while 1:
            try:
                data, addres = sock.recvfrom(1024)
                text_utf = data.decode('utf-8')
                print("\033[40m\033[1m\033[37m", addres[0], addres[1], '\n', text_utf, '\n')

                if addres not in client:
                    client.append(addres)  # Если такого клиента нету , то добавить
                for clients in client:
                    if clients == addres:
                        sock.sendto(b'You have been joined to the server', clients)
                        # отправлять данные клиенту, который их прислал
                    sock.sendto(data, clients)
            except ConnectionResetError:
                data, addres = sock.recvfrom(1024)
                print(
                    f"Удаленный хост принудительно разорвал существующее подключение\nПроцесс продолжает свою работу\n{data, addres}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Example()
    window.setObjectName("MainWindow")
    window.setStyleSheet(qdarktheme.load_stylesheet(custom_colors={'foreground>input.placeholder': '#D0BCFF',
                                                                    "primary": "#D0BCFF", 'border': '#202124'}))
    window.show()
    app.exec()
    app_icon = QtGui.QIcon()
    app_icon.addFile('icon.jpg', QtCore.QSize(16, 16))
    app.setWindowIcon(app_icon)

