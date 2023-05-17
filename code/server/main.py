from varibles import *

class Server(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.IP_box = None
        self.all_exit = None
        self.Exit_menu = None
        self.btn = None
        self.Password_box = None
        self.Address_box = None
        self.init_ui()
        self.exit = True
        self.old_pos = None
        self.lbl = QLabel(self)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

    def init_ui(self) -> None:
        self.setGeometry(300, 300, 150, 175)
        self.setWindowTitle('Server_Window')
        self.setStyleSheet(qdarktheme.load_stylesheet(custom_colors={"primary": "#D0BCFF"}))

        self.lbl = QLabel(self)
        self.lbl.setText('ip')
        self.lbl.move(0, -5)

        self.lbl = QLabel(self)
        self.lbl.setText('address')
        self.lbl.move(0, 20)

        self.lbl = QLabel(self)
        self.lbl.setText('code')
        self.lbl.move(0, 50)
        self.IP_box = QLineEdit(self)
        self.IP_box.resize(100, 20)
        self.IP_box.move(50, 0)

        self.Address_box = QLineEdit(self)
        self.Address_box.resize(100, 20)
        self.Address_box.move(50, 25)

        self.Password_box = QLineEdit(self)
        self.Password_box.resize(100, 20)
        self.Password_box.move(50, 50)

        self.btn = QPushButton('update', self)
        self.btn.resize(150, 20)
        self.btn.move(0, 75)
        self.btn.clicked.connect(self.update)
        self.btn = QPushButton('start_server', self)
        self.btn.resize(150, 20)
        self.btn.move(0, 100)
        self.btn.clicked.connect(self.starting_server)
        self.Exit_menu = QPushButton('exit from settings', self)
        self.Exit_menu.resize(150, 20)
        self.Exit_menu.move(0, 125)
        self.Exit_menu.clicked.connect(self.exit_menu)
        self.all_exit = QPushButton('exit', self)
        self.all_exit.resize(150, 20)
        self.all_exit.move(0, 150)
        self.all_exit.clicked.connect(self.all_exit_program)

    def all_exit_program(self) -> None:
        Server.close(self)

    def exit_menu(self) -> None:
        Server.hide(self)

    def update(self) -> None:
        global IPServer, AddressServer, PasswordCode, sock, start
        IPServer = str(self.IP_box.text())
        AddressServer = int(self.Address_box.text())
        PasswordCode = str(self.Password_box.text())
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sock.bind((str(IPServer),
                       int(AddressServer)))
            print("ip/address установлен успешно")
        except OSError:
            print("Вы забыли сменить ip/address")
        start = True

    # вызывается при нажатии кнопки мыши
    def mousePressEvent(self, event) -> None:
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.old_pos = event.pos()

    # вызывается при отпускании кнопки мыши
    def mouseReleaseEvent(self, event) -> None:
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.old_pos = None

    # вызывается всякий раз, когда мышь перемещается
    def mouseMoveEvent(self, event) -> None:
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)

    @staticmethod
    def starting_server() -> None:
        global start
        if start:
            t1 = threading.Thread(target=server_windows)
            t1.start()
            print('\033[40mStart Server')
            print('enabling the server\n')
            start = False
        else:
            print("обновите IpAddress")

def server_windows():
    global sock, client, groups, sock
    global start, PasswordCode, temporary_list
    if start:
        while 1:
            try:
                data, addres = sock.recvfrom(1024)
                text_utf = data.decode('utf-8')
                print(text_utf)


                if addres not in client:
                    if str(PasswordCode) == '':
                        client.append(addres)
                    else:
                        if addres not in temporary_list:
                            sock.sendto('Введите пароль сервера:'.encode('utf-8'), addres)
                            temporary_list.append(addres)  # Если такого клиента нету , то добавить

                        elif addres in temporary_list:
                            if text_utf == PasswordCode:
                                print('good job')
                                sock.sendto('Пароль введен верно. Вы вошли на сервер'.encode('utf-8'), addres)
                                client.append(addres)
                            else:
                                sock.sendto('Введите пароль сервера:'.encode('utf-8'), addres)

                for clients in client:
                    if clients == addres:
                        continue  # Не отправлять данные клиенту, который их прислал

                    sock.sendto(data, clients)

            except ConnectionResetError:
                data, addres = sock.recvfrom(1024)
                print(
                    f"Удаленный хост принудительно разорвал существующее подключение\n"
                    f"Процесс продолжает свою работу\n"
                    f"{data}{addres}", )
                for clients in client:
                    if clients == addres:
                        continue  # Не отправлять данные клиенту, который их прислал
                    sock.sendto(data, clients)
