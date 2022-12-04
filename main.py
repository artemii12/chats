import sys
import qdarktheme
import socket
import pickle
import threading
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt6 import QtGui, QtCore


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.chats = ['', '', '', '', '', '', '', '']


        self.password = {"darling": "1234", "1": "1"}
        self.on = False
        self.login = ''

    def initUI(self):
        self.setGeometry(1000, 600, 450, 0)
        self.setWindowTitle('UNKNOWN INCOMING')
        self.setWindowIcon(QtGui.QIcon('cff.jpg'))

        self.btn0 = QPushButton(' registration', self)
        self.btn0.resize(self.btn0.sizeHint())
        self.btn0.move(375, 0)
        self.btn0.resize(75, 25)
        self.btn0.clicked.connect(self.registr)

        self.lbl = QLabel(self)
        self.lbl.setText('LOGIN  ')
        self.lbl.resize(self.lbl.sizeHint())
        self.lbl.move(197, 10)

        self.textBox1 = QLineEdit(self)
        self.textBox1.resize(150, 20)
        self.textBox1.move(143, 35)

        self.lbl1 = QLabel(self)
        self.lbl1.setText('PASSWORD  ')
        self.lbl1.resize(self.lbl1.sizeHint())
        self.lbl1.move(185, 60)

        self.textBox2 = QLineEdit(self)
        self.textBox2.resize(150, 20)
        self.textBox2.move(143, 85)
        self.textBox2.setEchoMode(QLineEdit.EchoMode.Password)
        self.btn = QPushButton('ENTER', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(180, 110)

        self.btn.clicked.connect(self.check)

        self.lbl2 = QLabel(self)
        self.lbl3 = QLabel(self)
        self.lbl4 = QLabel(self)
        self.lbl5 = QLabel(self)
        self.lbl6 = QLabel(self)
        self.lbl7 = QLabel(self)
        self.lbl8 = QLabel(self)
        self.lbl9 = QLabel(self)

        self.textBox3 = QLineEdit(self)
        self.textBox3.setVisible(False)

        self.textBox4 = QLineEdit(self)
        self.textBox4.setVisible(False)

        self.textBox5 = QLineEdit(self)
        self.textBox5.setVisible(False)

        self.btn1 = QPushButton('>', self)
        self.btn1.setVisible(False)
        self.btn1.clicked.connect(self.update_message)

        self.btn2 = QPushButton('->', self)
        self.btn2.setVisible(False)
        self.btn2.clicked.connect(self.now_ip)

    def now_ip(self):
        self.server = self.textBox4.text(), int(self.textBox5.text())
    def read_sok(self):
        while 1:
            data = self.sor.recv(1024)
            self.text_utf = data.decode('utf-8')

            self.chats.append(self.text_utf)
            del self.chats[0]
            self.lbl2.setText(f'{self.chats[0]}')
            self.lbl2.resize(self.lbl2.sizeHint())
            self.lbl3.setText(f'{self.chats[1]}')
            self.lbl3.resize(self.lbl3.sizeHint())
            self.lbl4.setText(f'{self.chats[2]}')
            self.lbl4.resize(self.lbl4.sizeHint())
            self.lbl5.setText(f'{self.chats[3]}')
            self.lbl5.resize(self.lbl5.sizeHint())
            self.lbl6.setText(f'{self.chats[4]}')
            self.lbl6.resize(self.lbl6.sizeHint())

            self.lbl7.setText(f'{self.chats[5]}')
            self.lbl7.resize(self.lbl7.sizeHint())
            self.lbl8.setText(f'{self.chats[6]}')
            self.lbl8.resize(self.lbl8.sizeHint())
            self.lbl9.setText(f'{self.chats[7]}')
            self.lbl9.resize(self.lbl9.sizeHint())

    def update_message(self):
        self.text = self.textBox3.text()
        self.chat_groups = self.textBox4.text()
        self.sor.sendto(('[' + self.login + ']' + self.text).encode('utf-8'), self.server)
        self.potok = threading.Thread(target=self.read_sok)
        self.potok.start()
        self.chats.append(self.text)
        del self.chats[0]
        self.lbl2.setText(f'{self.chats[0]}')
        self.lbl2.resize(self.lbl2.sizeHint())
        self.lbl3.setText(f'{self.chats[1]}')
        self.lbl3.resize(self.lbl3.sizeHint())
        self.lbl4.setText(f'{self.chats[2]}')
        self.lbl4.resize(self.lbl4.sizeHint())
        self.lbl5.setText(f'{self.chats[3]}')
        self.lbl5.resize(self.lbl5.sizeHint())
        self.lbl6.setText(f'{self.chats[4]}')
        self.lbl6.resize(self.lbl6.sizeHint())

        self.lbl7.setText(f'{self.chats[5]}')
        self.lbl7.resize(self.lbl7.sizeHint())
        self.lbl8.setText(f'{self.chats[6]}')
        self.lbl8.resize(self.lbl8.sizeHint())
        self.lbl9.setText(f'{self.chats[7]}')
        self.lbl9.resize(self.lbl9.sizeHint())

    def check(self):
        if self.on:
            self.add_account()
        else:
            self.count()

    def add_account(self):
        login = self.textBox1.text()
        password = self.textBox2.text()
        self.password[login] = password
        self.textBox1.setText('you are registered')
        self.textBox2.setText('')
        self.registr()
        print(self.password)

    def registr(self):
        self.lbl.setText('LOGIN  ')
        self.lbl1.setText('PASSWORD  ')
        if self.on:
            self.btn0.setText(' registration')
            self.btn.setText("enter")
            self.lbl.setText('LOGIN  ')
            self.lbl.resize(self.lbl1.sizeHint())
            self.lbl.move(197, 10)
            self.lbl1.setText('PASSWORD  ')
            self.lbl1.resize(self.lbl1.sizeHint())
            self.lbl1.move(185, 60)
            self.on = False
        else:
            self.btn0.setText('entrance')
            self.btn.setText("register")
            self.lbl.setText('NEW NICKNAME')
            self.lbl.resize(self.lbl.sizeHint())
            self.lbl.move(170, 10)
            self.lbl1.setText('NOW PASSWORD')
            self.lbl1.resize(self.lbl1.sizeHint())
            self.lbl1.move(170, 60)
            self.on = True

    def count(self):
        self.login = self.textBox1.text()
        password = self.textBox2.text()
        for i in self.password.keys():
            if self.login in i:
                if password == self.password[i]:
                    self.server = '192.168.3.4', 25525  # Данные сервера
                    self.sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    self.sor.bind(('', 0))  # Задаем сокет как клиент

                    self.sor.sendto((self.login + ' Connect to server').encode('utf-8'),
                                    self.server)  # Уведомляем сервер о подключении

                    self.lbl.deleteLater()
                    self.textBox1.deleteLater()
                    self.lbl1.deleteLater()
                    self.textBox2.deleteLater()
                    self.btn.deleteLater()
                    self.setWindowTitle('CHAT')

                    self.lbl2.setText(f'{self.chats[4]}')
                    self.lbl2.resize(self.lbl2.sizeHint())
                    self.lbl2.move(0, 0)

                    self.lbl3.setText(f'{self.chats[0]}')
                    self.lbl3.resize(self.lbl3.sizeHint())
                    self.lbl3.move(0, 15)

                    self.lbl4.setText(f'{self.chats[1]}')
                    self.lbl4.resize(self.lbl4.sizeHint())
                    self.lbl4.move(0, 30)

                    self.lbl5.setText(f'{self.chats[2]}')
                    self.lbl5.resize(self.lbl5.sizeHint())
                    self.lbl5.move(0, 45)

                    self.lbl6.setText(f'{self.chats[3]}')
                    self.lbl6.resize(self.lbl6.sizeHint())
                    self.lbl6.move(0, 60)

                    self.lbl7.setText(f'{self.chats[5]}')
                    self.lbl7.resize(self.lbl6.sizeHint())
                    self.lbl7.move(0, 75)

                    self.lbl8.setText(f'{self.chats[6]}')
                    self.lbl8.resize(self.lbl6.sizeHint())
                    self.lbl8.move(0, 90)

                    self.lbl9.setText(f'{self.chats[7]}')
                    self.lbl9.resize(self.lbl6.sizeHint())
                    self.lbl9.move(0, 105)

                    self.btn1.resize(self.btn.sizeHint())
                    self.btn1.resize(25, 25)
                    self.btn1.move(425, 125)
                    self.btn1.setVisible(True)

                    self.textBox3.resize(425, 20)
                    self.textBox3.move(0, 125)
                    self.textBox3.setVisible(True)

                    self.textBox4.setText("interlocutor ip")
                    self.textBox4.resize(75, 20)
                    self.textBox4.move(299, 0)
                    self.textBox4.setVisible(True)

                    self.textBox5.setText("adress")
                    self.textBox5.resize(50, 20)
                    self.textBox5.move(375, 0)
                    self.textBox5.setVisible(True)
                    self.btn0.setVisible(False)

                    self.btn2.resize(self.btn.sizeHint())
                    self.btn2.resize(24, 24)
                    self.btn2.move(425, 0)
                    self.btn2.setVisible(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Example()
    window.show()
    app.setStyleSheet(qdarktheme.load_stylesheet())
    app_icon = QtGui.QIcon()
    app_icon.addFile('cff.jpg', QtCore.QSize(16, 16))
    app.setWindowIcon(app_icon)
    app.exec()
