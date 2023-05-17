from variables import *

"""def read_sok():
    while 1 :
        data = sor.recv(1024)
        print(data.decode('utf-8'))"""


server = ip, Address  # Данные сервера

sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sor.bind(('', 0))  # Задаем сокет как клиент
def connecting_to_server():
    print(f'{ip} {Address}')
    sor.sendto((f'{login_} Connect to server').encode('utf-8'), (ip, Address))  # Уведомляем сервер о подключении

"""potok = threading.Thread(target= read_sok)
potok.start()"""

def now_message(input = str) -> None:
    sor.sendto((f'[{login_}] {input}').encode('utf-8'), (ip, Address))
