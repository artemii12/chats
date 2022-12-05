import socket
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('192.168.3.4', 25524))
client = [] # Массив где храним адреса клиентов
groups = []
print('\033[40mStart Server')
print('enabling the server')
password = {"darling": "1234"}

while 1:

    data, addres = sock.recvfrom(1024)
    print(data, addres)
    text_utf = data.decode('utf-8')
    print("\033[40m\033[1m\033[37m", addres[0], addres[1], '\n', text_utf, '\n')

    if addres not in client:
        client.append(addres)  # Если такого клиента нету , то добавить

    for clients in client:
        if clients == addres:
            continue  # Не отправлять данные клиенту, который их прислал

        sock.sendto(data, clients)

