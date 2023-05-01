from variables import *
from encoding import decode

def updating_settings(self):
    global decode
    self.setGeometry(1455, 650, 200, 250)
    self.setWindowTitle('UNKNOWN INCOMING')
    self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
    self.setStyleSheet(qdarktheme.load_stylesheet(custom_colors={"primary": "#D0BCFF"}))

    self.btn_registration = QPushButton('updating the decoder', self)
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

    self.encode = QLineEdit(self)
    self.encode.setText(str(decode))
    self.encode.resize(70, 25)
    self.encode.move(130, 0)
