import socket
import sys
import threading
import qdarktheme
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, \
    QLabel, QLineEdit, QWidget, QCheckBox
from PyQt6 import QtGui, QtCore
#  192.168.3.4
#  25525
IP = ''
Address = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, Address))
client = []  # Массив где храним адреса клиентов
groups = []
password = {"darling": "1234"}
start = False
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.exit = True
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        custom_colors = {"background": "#bcacd4",
                         "border": "#d596fa",
                         "foreground": "#18047e",
                         "primary": "#8624e4",
                         "input.background": "#d596fa",
                         "inputButton.hoverBackground": "#18047e"}
        self.setStyleSheet(qdarktheme.load_stylesheet(custom_colors=custom_colors))

    def initUI(self):
        self.setGeometry(300, 300, 150, 123)
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


        self.Exit_menu = QPushButton('exiting the program', self)
        self.Exit_menu.resize(150, 20)
        self.Exit_menu.move(0, 100)
        self.Exit_menu.clicked.connect(self.exit_menu)

    def exit_menu(self):
        del Example

    def update(self):
        global IP, Address, sock, start
        IP = str(self.IP_box.text())
        Address = int(self.Address_box.text())
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.bind((str(self.IP_box.text()),
                   int(self.Address_box.text())))

        start = True

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
                print(client)  # список [[ip id]]
                print(data)  # текст отправителя

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
    window.show()
    app.exec()
    app_icon = QtGui.QIcon()
    app_icon.addFile('cff.jpg', QtCore.QSize(16, 16))
    app.setWindowIcon(app_icon)

