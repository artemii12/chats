import sys
import qdarktheme
import socket
import threading
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, \
    QLabel, QLineEdit, QWidget, QCheckBox, QMessageBox, QToolBar
from PyQt6 import QtGui, QtCore
import sqlite3
from encoding import encode_, decode, decode_, ALPHA
from variables import ip, Address, update_mas, system_update, dark, custom_colors, update_ip, exit_
from creating_objects import updating_settings
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
class instance(QMainWindow):
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

        def update(self) -> None:
            updating_settings(self=self)

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

        def now_ip(self, s):
            global ip, Address, update_mas, update_ip

            self.reply = QMessageBox(self)
            self.reply.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)

            self.reply.move(self.geometry().x(), self.geometry().y()-100)
            self.reply.setText("Вы уверены что хотите сменить ipaddress")
            self.reply.setStandardButtons(QMessageBox.StandardButton.Yes |
                                     QMessageBox.StandardButton.No)
            self.reply.setIcon(QMessageBox.Icon.Question)
            x = self.reply.exec()

            if x == QMessageBox.StandardButton.Yes:
                try:
                    ip = str(self.interlocutor_ip.text())
                    Address = int(self.interlocutor_adress.text())
                    update_ip = True
                    update_mas = True
                except ValueError:
                    self.interlocutor_ip.setText("interlocutor ip")
                    self.interlocutor_adress.setText("Address")

        def exit_menu(self):
            global decode
            try:
                decode = int(self.encode.text())
            except:
                self.encode.setText("3")

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
            """массивная ошибка"""
        if ip != '' and update_ip:
            self.server = ip, Address  # Данные сервера
            self.sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sor.bind(('', 0))  # Задаем сокет как клиент
            try:
                self.sor.sendto((self.login + ' Connect to server').encode('utf-8'),
                                self.server)  # Уведомляем сервер о подключении
            except socket.gaierror as ert:
                pass
            update_ip = False

        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Return:
            self.update_message()
    def test1(self):
        print(453)

    def init_ui(self):
        self.setGeometry(1000, 650, 450, 200)
        self.setWindowTitle('UNKNOWN INCOMING')
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)



        self.text_LOGIN = QLabel(self)
        self.text_LOGIN.setText('LOGIN  ')
        self.text_LOGIN.resize(self.text_LOGIN.sizeHint())
        self.text_LOGIN.move(197, 40)



        self.text_PASSWORD = QLabel(self)
        self.text_PASSWORD.setText('PASSWORD  ')
        self.text_PASSWORD.resize(self.text_PASSWORD.sizeHint())
        self.text_PASSWORD.move(185, 90)

        self.textBox1 = QLineEdit(self)
        self.textBox1.resize(150, 20)
        self.textBox1.move(143, 65)

        self.textBox2 = QLineEdit(self)
        self.textBox2.resize(150, 20)
        self.textBox2.move(143, 115)
        self.textBox2.setEchoMode(QLineEdit.EchoMode.Password)

        self.textBox3 = QLineEdit(self)
        self.textBox3.setVisible(False)

        self.btn_enter_registr = QPushButton('ENTER', self)
        self.btn_enter_registr.resize(self.btn_enter_registr.sizeHint())
        self.btn_enter_registr.move(194, 145)
        self.btn_enter_registr.clicked.connect(self.check)

        for i in range(1, 9):
            exec(f'self.sms_text_{i} = QLabel(self)')

        self.sending_sms = QPushButton('>', self)
        self.sending_sms.setVisible(False)
        self.sending_sms.clicked.connect(self.update_message)
        self.update_setting()

        self.menu = self.menuBar()

        self.registers = QAction("&Регистрация", self)
        self.registers.setStatusTip("This is your button")
        self.registers.triggered.connect(self.registration)
        self.menu.addAction(self.registers)


        self.exit_gl_menu = QAction("Выход", self)
        self.exit_gl_menu.setStatusTip("This is your button")
        self.exit_gl_menu.triggered.connect(self.sys_exit)
        self.menu.addAction(self.exit_gl_menu)



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

        sys.exit()

    def read_sok(self):
        global decode
        while exit_:
            print("activet")
            try:
                data = self.sor.recv(1024)
                self.text_utf = data.decode('utf-8')
                print(self.text_utf)
                text = encode_(self.text_utf, decode)
                print(text)
                self.chats.append(text)
                del self.chats[0]

            except ConnectionResetError:
                self.text_utf = 'Удаленный хост принудительно разорвал существующее подключение'
                self.chats.append(self.text_utf)
                del self.chats[0]
            for i in range(1, 9):
                exec(f'self.sms_text_{i}.setText(f"{self.chats[i - 1]}")')
                exec(f'self.sms_text_{i}.resize(self.sms_text_{i}.sizeHint())')

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
        if ip == '':
            self.chats.append('ip and address were not added to the settings')
            del self.chats[0]
        else:
            if update_mas:
                """массивная ошибка"""
                try:
                    self.sor.sendto((decode_(self.login + ' Connect to server', decode)).encode('utf-8'),
                                    self.server)  # Уведомляем сервер о подключении
                except socket.gaierror as ert:
                    self.server = ip, Address
                    self.chats.append(f'Не верно введен ip|adress {self.server[0], self.server[1]}')
                    del self.chats[0]
                self.potok = threading.Thread(target=self.read_sok)
                self.potok.start()
                self.chats.append(f'the ip address is not verified: {ip}:{Address}')
                del self.chats[0]
            try:
            # отправка сообщений
                self.sor.sendto((decode_(str('[' + self.login + ']' + self.text), decode)).encode('utf-8'), self.server)
            except:
                self.chats.append(f'the ip address is not verified: {ip}:{Address}')
                del self.chats[0]
            update_mas = False
        self.chats.append(f'[{self.login}]-{self.text}')
        del self.chats[0]
        for i in range(1, 9):
            exec(f'self.sms_text_{i}.setText(f"{self.chats[i - 1]}")')
            exec(f'self.sms_text_{i}.resize(self.sms_text_{i}.sizeHint())')
        self.textBox3.setText('')

    def check(self):
        if self.on:
            self.add_account()
        else:
            self.count()

    def add_account(self):
        conn = sqlite3.connect('system_data.db')
        c = conn.cursor()
        login = self.textBox1.text()
        password = self.textBox2.text()
        c.execute("INSERT INTO data (name, password) VALUES(?, ?)",
                  (login, password))
        self.textBox1.setText('you are registered')
        self.textBox2.setText('')
        conn.commit()
        c.close()
        conn.close()
        self.registration()

    def registration(self):
        self.text_LOGIN.setText('LOGIN  ')
        self.text_PASSWORD.setText('PASSWORD  ')
        if self.on:
            self.btn_enter_registr.setText("ENTER")
            self.btn_enter_registr.resize(self.btn_enter_registr.sizeHint())
            self.btn_enter_registr.move(194, 145)
            self.text_LOGIN.setText('LOGIN  ')
            self.text_LOGIN.resize(self.text_PASSWORD.sizeHint())
            self.text_LOGIN.move(197, 40)
            self.text_PASSWORD.setText('PASSWORD  ')
            self.text_PASSWORD.resize(self.text_PASSWORD.sizeHint())
            self.text_PASSWORD.move(185, 90)
            self.registers.setText("регистрация")
            self.on = False
        else:
            self.btn_enter_registr.setText("REGISTER")
            self.btn_enter_registr.resize(self.btn_enter_registr.sizeHint())
            self.btn_enter_registr.move(185, 145)
            self.text_LOGIN.setText('NEW NICKNAME')
            self.text_LOGIN.resize(self.text_LOGIN.sizeHint())
            self.text_LOGIN.move(170, 40)
            self.text_PASSWORD.setText('NOW PASSWORD')
            self.text_PASSWORD.resize(self.text_PASSWORD.sizeHint())
            self.text_PASSWORD.move(170, 90)
            self.registers.setText("вход")
            self.on = True

    def count(self):
        global ip, Address
        self.login = self.textBox1.text()
        self.password = self.textBox2.text()
        if ip == '':
            self.sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sor.bind(('', 0))  # Задаем сокет как клиент
        else:
            self.server = ip, Address  # Данные сервера
            self.sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sor.bind(('', 0))  # Задаем сокет как клиент

            self.sor.sendto((self.login + ' Connect to server').encode('utf-8'),
                            self.server)  # Уведомляем сервер о подключении

        sql = sqlite3.connect('system_data.db')
        cursor = sql.cursor()
        sqlite_select_query = """SELECT * from data"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for name, password in records:
            if str(self.login) == str(name):
                if str(self.password) == str(password):
                    print(65)
                    self.text_LOGIN.setVisible(False)
                    self.textBox1.setVisible(False)
                    self.text_PASSWORD.setVisible(False)
                    self.textBox2.setVisible(False)
                    self.btn_enter_registr.setVisible(False)

                    self.registers.deleteLater()
                    self.exit_gl_menu.deleteLater()

                    self.button_action1 = QAction("Настройка цветов", self)
                    self.button_action1.setStatusTip("This is your button")
                    self.button_action1.triggered.connect(self.settings_window)

                    self.button_action2 = QAction("Настройка IP.address", self)
                    self.button_action2.setStatusTip("This is your button")
                    self.button_action2.triggered.connect(self.settings_window)

                    self.button_action3 = QAction("Настройка кодирования", self)
                    self.button_action3.setStatusTip("This is your button")
                    self.button_action3.triggered.connect(self.settings_window)

                    self.fileMenu = self.menu.addMenu("Настройки")
                    self.fileMenu.addAction(self.button_action1)
                    self.fileMenu.addAction(self.button_action2)
                    self.fileMenu.addAction(self.button_action3)

                    self.exit_gl_menu = QAction("Выход", self)
                    self.exit_gl_menu.setStatusTip("This is your button")
                    self.exit_gl_menu.triggered.connect(self.sys_exit)
                    self.menu.addAction(self.exit_gl_menu)




                    self.setWindowTitle('CHAT')
                    for i in range(1, 9):
                        exec(f'self.sms_text_{i}.setText(f"{self.chats[0]}")')
                        exec(f'self.sms_text_{i}.resize(self.sms_text_{i}.sizeHint())')
                        if i == 1:
                            exec(f'self.sms_text_{i}.move(0, 30)')
                        else:
                            exec(f'self.sms_text_{i}.move( 0, (15*({i}-1))+30 )')

                    self.sending_sms.resize(self.btn_enter_registr.sizeHint())
                    self.sending_sms.resize(25, 25)
                    self.sending_sms.move(425, 170)
                    self.sending_sms.setVisible(True)

                    self.textBox3.resize(425, 20)
                    self.textBox3.move(0, 170)
                    self.textBox3.setVisible(True)
