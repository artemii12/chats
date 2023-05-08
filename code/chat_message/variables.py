import sys
import socket
import sqlite3
import threading
import qdarktheme
from screeninfo import get_monitors
from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QWidget, QCheckBox, QMessageBox, QToolBar
from encoding import encode_, decode, decode_, ALPHA
def pos():
    monitor = [(m.width/2, m.height/2) for m in get_monitors()]
    return monitor[0]
ip, Address, update_mas, system_update, dark, custom_colors, update_ip, exit_, login_ = '', 0, False, False, 0, {}, False, True, ''