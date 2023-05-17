import sys
import socket
import threading
import qdarktheme
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, \
    QLabel, QLineEdit

#  192.168.3.4
#  25525

IPServer = ''
AddressServer = 0
PasswordCode = ''
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IPServer, AddressServer))
client = []  # Массив где храним адреса клиентов
groups = []
start = False