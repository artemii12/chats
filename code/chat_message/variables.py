import sys
import qdarktheme
import socket
import threading
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, \
    QLabel, QLineEdit, QWidget, QCheckBox, QMessageBox, QToolBar
from pynput.mouse import Controller
from PyQt6 import QtGui, QtCore
import sqlite3
import functools
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from encoding import encode_, decode, decode_, ALPHA

ip = ''
Address = 0
update_mas = False
system_update = False
dark = 0
custom_colors = {}
update_ip = False
exit_ = True
login_ = ''
