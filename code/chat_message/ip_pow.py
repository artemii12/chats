from PyQt6.QtWidgets import QMessageBox
from PyQt6 import QtCore


def now_ip1(self):
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
            ip = str(self.interlocutor_ip1.text())
            Address = int(self.interlocutor_adress1.text())
            update_ip = True
            update_mas = True
        except ValueError:
            self.interlocutor_ip1.setText("interlocutor ip")
            self.interlocutor_adress1.setText("Address")
def now_ip2(self):
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
            ip = str(self.interlocutor_ip2.text())
            Address = int(self.interlocutor_adress2.text())
            update_ip = True
            update_mas = True
        except ValueError:
            self.interlocutor_ip2.setText("interlocutor ip")
            self.interlocutor_adress2.setText("Address")

def now_ip3(self):
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
            ip = str(self.interlocutor_ip3.text())
            Address = int(self.interlocutor_adress3.text())
            update_ip = True
            update_mas = True
        except ValueError:
            self.interlocutor_ip3.setText("interlocutor ip")
            self.interlocutor_adress3.setText("Address")

def now_ip4(self):
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
            ip = str(self.interlocutor_ip4.text())
            Address = int(self.interlocutor_adress4.text())
            update_ip = True
            update_mas = True
        except ValueError:
            self.interlocutor_ip4.setText("interlocutor ip")
            self.interlocutor_adress4.setText("Address")

def now_ip5(self):
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
            ip = str(self.interlocutor_ip5.text())
            Address = int(self.interlocutor_adress5.text())
            update_ip = True
            update_mas = True
        except ValueError:
            self.interlocutor_ip5.setText("interlocutor ip")
            self.interlocutor_adress5.setText("Address")
