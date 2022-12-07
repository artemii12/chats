import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('192.168.3.4', 25525))
client = []  # Массив где храним адреса клиентов
groups = []
print('\033[40mStart Server')
print('enabling the server\n')
password = {"darling": "1234"}

while 1:
    try:
        data, addres = sock.recvfrom(1024)
        text_utf = data.decode('utf-8')
        print("\033[40m\033[1m\033[37m", addres[0], addres[1], '\n', text_utf, '\n')
        print(client)  # список [[ip id]]
        print(data)  # текст отправителя

        if addres not in client:
            client.append(addres)  # Если такого клиента нету , то добавить
        client_text = client
        for clients in client:
            if clients == addres:
                sock.sendto(b'You have been joined to the server', clients)
                # отправлять данные клиенту, который их прислал
            sock.sendto(data, clients)
    except ConnectionResetError:
        data, addres = sock.recvfrom(1024)
        print(f"Удаленный хост принудительно разорвал существующее подключение\nПроцесс продолжает свою работу\n{data,addres}")



