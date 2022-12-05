import sys
import qdarktheme
import socket

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt6 import QtGui, QtCore
import threading

class setting_window_menu(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.update()

    def update(self):
        self.setGeometry(1455, 650, 200, 0)
        self.setWindowTitle('UNKNOWN INCOMING')
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.btn_registration = QPushButton('  update the system  ', self)
        self.btn_registration.resize(self.btn_registration.sizeHint())
        self.btn_registration.move(0, 0)
        self.btn_registration.resize(self.btn_registration.sizeHint())
        self.btn_registration.clicked.connect(self.exit_menu)
    def exit_menu(self):
        pass

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.chats = ['', '', '', '', '', '', '', '']
        self.password = {"darling": "1234", "1": "1"}
        self.on = False
        self.login = ''
        self.window_setting = setting_window_menu()
        self.open = True

    def initUI(self):
        self.setGeometry(1000, 650, 450, 0)
        self.setWindowTitle('UNKNOWN INCOMING')
        self.setWindowIcon(QtGui.QIcon('cff.jpg'))
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

        self.btn_registration = QPushButton(' registration', self)
        self.btn_registration.resize(self.btn_registration.sizeHint())
        self.btn_registration.move(375, 0)
        self.btn_registration.resize(75, 25)
        self.btn_registration.clicked.connect(self.now_ip)

        self.text_LOGIN = QLabel(self)
        self.text_LOGIN.setText('LOGIN  ')
        self.text_LOGIN.resize(self.text_LOGIN.sizeHint())
        self.text_LOGIN.move(197, 10)

        self.textBox1 = QLineEdit(self)
        self.textBox1.resize(150, 20)
        self.textBox1.move(143, 35)

        self.text_PASSWORD = QLabel(self)
        self.text_PASSWORD.setText('PASSWORD  ')
        self.text_PASSWORD.resize(self.text_PASSWORD.sizeHint())
        self.text_PASSWORD.move(185, 60)

        self.textBox2 = QLineEdit(self)
        self.textBox2.resize(150, 20)
        self.textBox2.move(143, 85)
        self.textBox2.setEchoMode(QLineEdit.EchoMode.Password)

        self.btn_enter_registr = QPushButton('ENTER', self)
        self.btn_enter_registr.resize(self.btn_enter_registr.sizeHint())
        self.btn_enter_registr.move(180, 110)
        self.btn_enter_registr.clicked.connect(self.check)

        self.sms_text_1 = QLabel(self)
        self.sms_text_2 = QLabel(self)
        self.sms_text_4 = QLabel(self)
        self.sms_text_5 = QLabel(self)
        self.sms_text_6 = QLabel(self)
        self.sms_text_7 = QLabel(self)
        self.sms_text_8 = QLabel(self)
        self.sms_text_9 = QLabel(self)

        self.textBox3 = QLineEdit(self)
        self.textBox3.setVisible(False)

        self.textBox4 = QLineEdit(self)
        self.textBox4.setVisible(False)

        self.btn_exit = QPushButton('EXIT', self)
        self.btn_exit.setVisible(False)
        self.btn_exit.clicked.connect(self.sys_exit)

        self.btn_settings = QPushButton('SETTINGS', self)
        self.btn_settings.setVisible(False)
        self.btn_settings.clicked.connect(self.settings_window)

        self.textBox5 = QLineEdit(self)
        self.textBox5.setVisible(False)

        self.sending_sms = QPushButton('>', self)
        self.sending_sms.setVisible(False)
        self.sending_sms.clicked.connect(self.update_message)

        self.btn_now_ip = QPushButton('->', self)
        self.btn_now_ip.setVisible(False)
        self.btn_now_ip.clicked.connect(self.now_ip)

    def settings_window(self):
        if self.open:
            self.window_setting.show()
            self.open = False
        else:
            self.window_setting.hide()
            self.open = True

    def sys_exit(self):
        sys.exit()
    def now_ip(self):
        try:
            self.server = self.textBox4.text(), int(self.textBox5.text())
            self.sor.sendto((self.login + ' Connect to server').encode('utf-8'),
                            self.server)  # Уведомляем сервер о подключении
        except:
            self.textBox4.setText('wrong ip')
            self.textBox5.setText('wrong id')
            self.server = '192.168.3.4', 25525
    def read_sok(self):
        while 1:
            data = self.sor.recv(1024)
            self.text_utf = data.decode('utf-8')
            self.chats.append(self.text_utf)
            del self.chats[0]
            self.sms_text_1.setText(f'{self.chats[0]}')
            self.sms_text_1.resize(self.sms_text_1.sizeHint())
            self.sms_text_2.setText(f'{self.chats[1]}')
            self.sms_text_2.resize(self.sms_text_2.sizeHint())
            self.sms_text_4.setText(f'{self.chats[2]}')
            self.sms_text_4.resize(self.sms_text_4.sizeHint())
            self.sms_text_5.setText(f'{self.chats[3]}')
            self.sms_text_5.resize(self.sms_text_5.sizeHint())
            self.sms_text_6.setText(f'{self.chats[4]}')
            self.sms_text_6.resize(self.sms_text_6.sizeHint())

            self.sms_text_7.setText(f'{self.chats[5]}')
            self.sms_text_7.resize(self.sms_text_7.sizeHint())
            self.sms_text_8.setText(f'{self.chats[6]}')
            self.sms_text_8.resize(self.sms_text_8.sizeHint())
            self.sms_text_9.setText(f'{self.chats[7]}')
            self.sms_text_9.resize(self.sms_text_9.sizeHint())

    def update_message(self):
        self.text = self.textBox3.text()
        self.chat_groups = self.textBox4.text()
        self.sor.sendto(('[' + self.login + ']' + self.text).encode('utf-8'), self.server)
        self.potok = threading.Thread(target=self.read_sok)
        self.potok.start()
        self.chats.append(f'[{self.login}]-{self.text}')
        del self.chats[0]
        self.sms_text_1.setText(f'{self.chats[0]}')
        self.sms_text_1.resize(self.sms_text_1.sizeHint())
        self.sms_text_2.setText(f'{self.chats[1]}')
        self.sms_text_2.resize(self.sms_text_2.sizeHint())
        self.sms_text_4.setText(f'{self.chats[2]}')
        self.sms_text_4.resize(self.sms_text_4.sizeHint())
        self.sms_text_5.setText(f'{self.chats[3]}')
        self.sms_text_5.resize(self.sms_text_5.sizeHint())
        self.sms_text_6.setText(f'{self.chats[4]}')
        self.sms_text_6.resize(self.sms_text_6.sizeHint())

        self.sms_text_7.setText(f'{self.chats[5]}')
        self.sms_text_7.resize(self.sms_text_7.sizeHint())
        self.sms_text_8.setText(f'{self.chats[6]}')
        self.sms_text_8.resize(self.sms_text_8.sizeHint())
        self.sms_text_9.setText(f'{self.chats[7]}')
        self.sms_text_9.resize(self.sms_text_9.sizeHint())

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
        self.text_LOGIN.setText('LOGIN  ')
        self.text_PASSWORD.setText('PASSWORD  ')
        if self.on:
            self.btn_registration.setText(' registration')
            self.btn_enter_registr.setText("enter")
            self.text_LOGIN.setText('LOGIN  ')
            self.text_LOGIN.resize(self.text_PASSWORD.sizeHint())
            self.text_LOGIN.move(197, 10)
            self.text_PASSWORD.setText('PASSWORD  ')
            self.text_PASSWORD.resize(self.text_PASSWORD.sizeHint())
            self.text_PASSWORD.move(185, 60)
            self.on = False
        else:
            self.btn_registration.setText('entrance')
            self.btn_enter_registr.setText("register")
            self.text_LOGIN.setText('NEW NICKNAME')
            self.text_LOGIN.resize(self.text_LOGIN.sizeHint())
            self.text_LOGIN.move(170, 10)
            self.text_PASSWORD.setText('NOW PASSWORD')
            self.text_PASSWORD.resize(self.text_PASSWORD.sizeHint())
            self.text_PASSWORD.move(170, 60)
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

                    self.text_LOGIN.setVisible(False)
                    self.textBox1.setVisible(False)
                    self.text_PASSWORD.setVisible(False)
                    self.textBox2.setVisible(False)
                    self.btn_enter_registr.setVisible(False)
                    self.setWindowTitle('CHAT')

                    self.sms_text_1.setText(f'{self.chats[4]}')
                    self.sms_text_1.resize(self.sms_text_1.sizeHint())
                    self.sms_text_1.move(0, 0)

                    self.sms_text_2.setText(f'{self.chats[0]}')
                    self.sms_text_2.resize(self.sms_text_2.sizeHint())
                    self.sms_text_2.move(0, 15)

                    self.sms_text_4.setText(f'{self.chats[1]}')
                    self.sms_text_4.resize(self.sms_text_4.sizeHint())
                    self.sms_text_4.move(0, 30)

                    self.sms_text_5.setText(f'{self.chats[2]}')
                    self.sms_text_5.resize(self.sms_text_5.sizeHint())
                    self.sms_text_5.move(0, 45)

                    self.sms_text_6.setText(f'{self.chats[3]}')
                    self.sms_text_6.resize(self.sms_text_6.sizeHint())
                    self.sms_text_6.move(0, 60)

                    self.sms_text_7.setText(f'{self.chats[5]}')
                    self.sms_text_7.resize(self.sms_text_6.sizeHint())
                    self.sms_text_7.move(0, 75)

                    self.sms_text_8.setText(f'{self.chats[6]}')
                    self.sms_text_8.resize(self.sms_text_6.sizeHint())
                    self.sms_text_8.move(0, 90)

                    self.sms_text_9.setText(f'{self.chats[7]}')
                    self.sms_text_9.resize(self.sms_text_6.sizeHint())
                    self.sms_text_9.move(0, 105)

                    self.sending_sms.resize(self.btn_enter_registr.sizeHint())
                    self.sending_sms.resize(25, 25)
                    self.sending_sms.move(425, 125)
                    self.sending_sms.setVisible(True)

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

                    self.btn_registration.setVisible(False)

                    self.btn_now_ip.resize(self.btn_enter_registr.sizeHint())
                    self.btn_now_ip.resize(24, 24)
                    self.btn_now_ip.move(425, 0)
                    self.btn_now_ip.setVisible(True)

                    self.btn_settings.resize(self.btn_exit.sizeHint())
                    self.btn_settings.move(350, 25)
                    self.btn_settings.resize(100, 25)
                    self.btn_settings.setVisible(True)

                    self.btn_exit.resize(self.btn_exit.sizeHint())
                    self.btn_exit.move(400, 50)
                    self.btn_exit.resize(50, 25)
                    self.btn_exit.setVisible(True)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Example()
    window.show()
    app.setStyleSheet(qdarktheme.load_stylesheet())
    app_icon = QtGui.QIcon()
    app_icon.addFile('cff.jpg', QtCore.QSize(16, 16))
    app.setWindowIcon(app_icon)
    app.exec()
