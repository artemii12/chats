from variables import *
sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sor.bind(('', 0))  # Задаем сокет как клиент
def connecting_to_server(ip = str, Address = int, login = str) -> None : sor.sendto((str(encode_(f'{login} Connect to server'))).encode('utf-8'), (ip, Address))
def now_message(ip = str, Address = int, login = str, text = str, decode = int) -> None: sor.sendto(((str(encode_(f'[{login}] {text}', decode)))).encode('utf-8'), (ip, Address))
def registr_password(ip = str, Address = int, text = str) -> None: sor.sendto((f'{text}').encode('utf-8'), (ip, Address))