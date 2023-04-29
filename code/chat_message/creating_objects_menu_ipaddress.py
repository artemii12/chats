from PyQt6.QtWidgets import QPushButton, \
    QLabel, QLineEdit, QCheckBox
from PyQt6 import QtCore
import qdarktheme
from encoding import decode
from PyQt6.QtWidgets import QPushButton, QLineEdit, QWidget, QMessageBox
from variables import ip, Address, update_mas, system_update, dark, custom_colors, update_ip, exit_

class SettingWindowMenuipaddress(QWidget):
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
        global decode
        self.setGeometry(1455, 650, 200, 100)
        self.setWindowTitle('UNKNOWN INCOMING')
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet(qdarktheme.load_stylesheet(custom_colors={"primary": "#D0BCFF"}))

        self.interlocutor_ip = QLineEdit(self)
        self.interlocutor_ip.setText("ip")
        self.interlocutor_ip.resize(75, 24)
        self.interlocutor_ip.move(25, 25)

        self.interlocutor_adress = QLineEdit(self)
        self.interlocutor_adress.setText("address")
        self.interlocutor_adress.resize(75, 24)
        self.interlocutor_adress.move(100, 25)

        self.btn_now_ip = QPushButton('apply', self)
        self.btn_now_ip.clicked.connect(self.now_ip)
        self.btn_now_ip.resize(self.btn_now_ip.sizeHint())
        self.btn_now_ip.resize(75, 24)
        self.btn_now_ip.move(100, 50)
        self.btn_now_ip.setVisible(True)

        self.exit = QPushButton('exit', self)
        self.exit.clicked.connect(self.yes_no)
        self.exit.resize(self.exit.sizeHint())
        self.exit.resize(75, 24)
        self.exit.move(25, 50)
        self.exit.setVisible(True)

    def yes_no(self):
        self.close()
        self.open1 = True

    def now_ip(self, s):
        global ip, Address, update_mas, update_ip

        self.reply = QMessageBox(self)
        self.reply.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)

        self.reply.move(self.geometry().x(), self.geometry().y() - 100)
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
