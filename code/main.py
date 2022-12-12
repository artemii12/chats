import sys

import qdarktheme
import socket
import threading
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, \
    QLabel, QLineEdit, QWidget, QCheckBox
from PyQt6 import QtGui, QtCore

ip = ''
Address = 0
update_mas = False
system_update = False
dark = 0
custom_colors = {}
update_ip = False

class main:
    class Example(QMainWindow):
        global ip, Address, update_mas, update_ip

        class SettingWindowMenu(QWidget):
            global ip, Address, update_mas, update_ip
            def __init__(self):
                super().__init__()
                self.update()
                self.old_pos = None

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

            def update(self):
                self.setGeometry(1455, 650, 200, 250)
                self.setWindowTitle('UNKNOWN INCOMING')
                self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
                self.setStyleSheet(qdarktheme.load_stylesheet(custom_colors={"primary": "#D0BCFF"}))

                self.btn_registration = QPushButton('  update the system  ', self)
                self.btn_registration.resize(self.btn_registration.sizeHint())
                self.btn_registration.move(0, 0)
                self.btn_registration.resize(self.btn_registration.sizeHint())
                self.btn_registration.clicked.connect(self.exit_menu)

                self.interlocutor_ip = QLineEdit(self)
                self.interlocutor_ip.setText("ip")
                self.interlocutor_ip.resize(77, 20)
                self.interlocutor_ip.move(0, 25)

                self.interlocutor_adress = QLineEdit(self)
                self.interlocutor_adress.setText("address")
                self.interlocutor_adress.resize(50, 20)
                self.interlocutor_adress.move(80, 25)

                self.btn_now_ip = QPushButton('->', self)
                self.btn_now_ip.clicked.connect(self.now_ip)
                self.btn_now_ip.resize(self.btn_now_ip.sizeHint())
                self.btn_now_ip.resize(24, 24)
                self.btn_now_ip.move(131, 25)
                self.btn_now_ip.setVisible(True)

                self.checkbox = QCheckBox("white theme", self)
                self.checkbox.move(0, 50)
                self.checkbox.resize(self.checkbox.sizeHint())
                self.checkbox.clicked.connect(self.yes_no)

                self.background = QLineEdit(self)
                self.background.setText("#bcacd4")
                self.background.resize(110, 20)
                self.background.move(0, 75)

                self.border = QLineEdit(self)
                self.border.setText("#d596fa")
                self.border.resize(110, 20)
                self.border.move(0, 100)

                self.foreground = QLineEdit(self)
                self.foreground.setText("#18047e")
                self.foreground.resize(110, 20)
                self.foreground.move(0, 125)

                self.primary = QLineEdit(self)
                self.primary.setText("#8624e4")
                self.primary.resize(110, 20)
                self.primary.move(0, 150)

                self.input_background = QLineEdit(self)
                self.input_background.setText("#d596fa")
                self.input_background.resize(110, 20)
                self.input_background.move(0, 175)

                self.inputButton_hoverBackground = QLineEdit(self)
                self.inputButton_hoverBackground.setText("#18047e")
                self.inputButton_hoverBackground.resize(110, 20)
                self.inputButton_hoverBackground.move(0, 200)

                self.text_background = QLabel(self)
                self.text_background.setText('background')
                self.text_background.resize(self.text_background.sizeHint())
                self.text_background.move(115, 75)

                self.text_border = QLabel(self)
                self.text_border.setText('border')
                self.text_border.resize(self.text_border.sizeHint())
                self.text_border.move(115, 100)

                self.text_foreground = QLabel(self)
                self.text_foreground.setText('foreground')
                self.text_foreground.resize(self.text_foreground.sizeHint())
                self.text_foreground.move(115, 125)

                self.text_primary = QLabel(self)
                self.text_primary.setText('primary')
                self.text_primary.resize(self.text_primary.sizeHint())
                self.text_primary.move(115, 150)

                self.text_input_background = QLabel(self)
                self.text_input_background.setText('input')
                self.text_input_background.resize(self.text_input_background.sizeHint())
                self.text_input_background.move(115, 172)
                self.text_input_background = QLabel(self)
                self.text_input_background.setText('background')
                self.text_input_background.resize(self.text_input_background.sizeHint())
                self.text_input_background.move(115, 180)

                self.text_inputButton_hoverBackground = QLabel(self)
                self.text_inputButton_hoverBackground.setText('inputButton')
                self.text_inputButton_hoverBackground.resize(self.text_inputButton_hoverBackground.sizeHint())
                self.text_inputButton_hoverBackground.move(115, 197)
                self.text_inputButton_hoverBackground = QLabel(self)
                self.text_inputButton_hoverBackground.setText('Background')
                self.text_inputButton_hoverBackground.resize(self.text_inputButton_hoverBackground.sizeHint())
                self.text_inputButton_hoverBackground.move(115, 205)

                self.text_foreground = QPushButton('UPDATE_COLORS', self)
                self.text_foreground.clicked.connect(self.update_colors)
                self.text_foreground.resize(self.text_foreground.sizeHint())
                self.text_foreground.move(0, 225)

            def update_colors(self):
                global custom_colors, dark, system_update
                background = self.background.text()
                border = self.border.text()
                foreground = self.foreground.text()
                primary = self.primary.text()
                input_background = self.input_background.text()
                input_button_hover_background = self.inputButton_hoverBackground.text()

                self.setStyleSheet(qdarktheme.load_stylesheet(custom_colors={"primary": "#D0BCFF"}))
                custom_colors = {"background": f"{background}",
                                 "border": f"{border}",
                                 "foreground": f"{foreground}",
                                 "primary": f"{primary}",
                                 "input.background": f"{input_background}",
                                 "inputButton.hoverBackground": f"{input_button_hover_background}"}
                self.setStyleSheet(qdarktheme.load_stylesheet(custom_colors=custom_colors))
                dark = 3
                system_update = True

            def yes_no(self):
                global dark, custom_colors
                if self.checkbox.isChecked():
                    dark = 1
                    self.setStyleSheet(qdarktheme.load_stylesheet("light"))
                if not self.checkbox.isChecked():
                    dark = 2
                    self.setStyleSheet(qdarktheme.load_stylesheet(custom_colors={"primary": "#D0BCFF"}))

            def now_ip(self):
                global ip, Address, update_mas, update_ip
                try:
                    ip = str(self.interlocutor_ip.text())
                    Address = int(self.interlocutor_adress.text())
                    update_ip = True
                    update_mas = True
                except ValueError:
                    self.interlocutor_ip.setText("interlocutor ip")
                    self.interlocutor_adress.setText("Address")

            def exit_menu(self):
                pass

        def __init__(self):
            global dark, timer
            super().__init__()
            self.setStyleSheet(qdarktheme.load_stylesheet())
            self.init_ui()
            self.chats = ['', '', '', '', '', '', '', '']
            self.password = {"darling": "1234", "1": "1"}
            self.on = False
            self.login = ''
            self.window_setting = self.SettingWindowMenu()
            self.open = True
            self.exit = False
            self.control = True
            self.old_pos = None
            self.update_ip = False

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
            global dark, update_ip
            if dark == 2:
                self.setStyleSheet(qdarktheme.load_stylesheet())
            if dark == 1:
                self.setStyleSheet(qdarktheme.load_stylesheet("light"))
            if dark == 3:
                self.setStyleSheet(qdarktheme.load_stylesheet(custom_colors=custom_colors))
                dark = 3

            if ip != '' and update_ip:
                self.server = ip, Address  # Данные сервера
                self.sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self.sor.bind(('', 0))  # Задаем сокет как клиент

                self.sor.sendto((self.login + ' Connect to server').encode('utf-8'),
                                self.server)  # Уведомляем сервер о подключении
                update_ip = False

            if not self.old_pos:
                return
            delta = event.pos() - self.old_pos
            self.move(self.pos() + delta)

        def init_ui(self):
            self.setGeometry(1000, 650, 450, 0)
            self.setWindowTitle('UNKNOWN INCOMING')
            self.setWindowIcon(QtGui.QIcon('../img/icon.jpg'))
            self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

            self.btn_registration = QPushButton(' registration', self)
            self.btn_registration.resize(self.btn_registration.sizeHint())
            self.btn_registration.move(375, 0)
            self.btn_registration.resize(75, 25)
            self.btn_registration.clicked.connect(self.registration)

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

            self.btn_exit = QPushButton('EXIT', self)
            self.btn_exit.setVisible(False)
            self.btn_exit.clicked.connect(self.sys_exit)

            self.btn_settings = QPushButton('SETTINGS', self)
            self.btn_settings.setVisible(False)
            self.btn_settings.clicked.connect(self.settings_window)

            self.sending_sms = QPushButton('>', self)
            self.sending_sms.setVisible(False)
            self.sending_sms.clicked.connect(self.update_message)
            self.update_setting()

        def update_setting(self):
            global dark
            if dark == 2:
                self.setStyleSheet(qdarktheme.load_stylesheet())
            if dark == 1:
                self.setStyleSheet(qdarktheme.load_stylesheet("light"))
            if dark == 3:
                self.setStyleSheet(qdarktheme.load_stylesheet(custom_colors=custom_colors))
                dark = 3

        def settings_window(self):
            global dark, custom_colors
            if self.open:
                self.window_setting.show()
                self.open = False
            else:
                if dark == 2:
                    self.setStyleSheet(qdarktheme.load_stylesheet())
                if dark == 1:
                    self.setStyleSheet(qdarktheme.load_stylesheet("light"))
                self.window_setting.hide()
                self.open = True
                if dark == 3:
                    self.setStyleSheet(qdarktheme.load_stylesheet(custom_colors=custom_colors))
                    dark = 3

        def sys_exit(self):
            self.exit = True
            if self.exit:
                self.exit = False
                sys.exit()

        def read_sok(self):
            while not self.exit:
                print(78)
                try:
                    print(1)
                    data = self.sor.recv(1024)
                    self.text_utf = data.decode('utf-8')
                    print(self.text_utf)
                    self.chats.append(self.text_utf)
                    del self.chats[0]

                except ConnectionResetError:
                    self.text_utf = 'Удаленный хост принудительно разорвал существующее подключение'
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
            global update_mas, ip, Address, error, dark, custom_colors, system_update, update_ip
            if dark == 2:
                self.setStyleSheet(qdarktheme.load_stylesheet())
            if dark == 1:
                self.setStyleSheet(qdarktheme.load_stylesheet("light"))
            if dark == 3:
                self.setStyleSheet(qdarktheme.load_stylesheet(custom_colors=custom_colors))
                dark = 3
                system_update = False

            self.text = self.textBox3.text()
            print(self.chats)
            if ip == '':
                self.chats.append('ip and address were not added to the settings')
                del self.chats[0]
            else:
                if update_mas:
                    try:
                        self.sor.sendto((self.login + ' Connect to server').encode('utf-8'),
                                        self.server)  # Уведомляем сервер о подключении
                    except:
                        print(98)
                        self.server = ip, Address
                        self.chats.append(f'Не верно введен ip|adress {self.server[0], self.server[1]}2')
                        del self.chats[0]
                    self.potok = threading.Thread(target=self.read_sok)
                    self.potok.start()
                    self.chats.append(f'the ip address is not verified: {ip}:{Address}')
                    del self.chats[0]
                # отправка сообщений
                print(self.chats)
                self.sor.sendto(('[' + self.login + ']' + self.text).encode('utf-8'), self.server)
                update_mas = False
            self.chats.append(f'[{self.login}]-{self.text}')
            del self.chats[0]
            print(self.chats)
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
            self.textBox3.setText('')

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
            self.registration()

        def registration(self):
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
            global ip, Address
            self.login = self.textBox1.text()
            password = self.textBox2.text()
            if ip == '':
                self.sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self.sor.bind(('', 0))  # Задаем сокет как клиент
            else:
                self.server = ip, Address  # Данные сервера
                self.sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self.sor.bind(('', 0))  # Задаем сокет как клиент

                self.sor.sendto((self.login + ' Connect to server').encode('utf-8'),
                                self.server)  # Уведомляем сервер о подключении
            for i in self.password.keys():
                if self.login in i:
                    if password == self.password[i]:
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

                        self.btn_settings.resize(self.btn_exit.sizeHint())
                        self.btn_settings.move(350, 0)
                        self.btn_settings.resize(100, 25)
                        self.btn_settings.setVisible(True)

                        self.btn_exit.resize(self.btn_exit.sizeHint())
                        self.btn_exit.move(400, 25)
                        self.btn_exit.resize(50, 25)
                        self.btn_exit.setVisible(True)
                        self.btn_registration.setVisible(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main.Example()
    window.show()
    app_icon = QtGui.QIcon()
    app_icon.addFile('icon.jpg', QtCore.QSize(16, 16))
    app.setWindowIcon(app_icon)
    app.exec()
