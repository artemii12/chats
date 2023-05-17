from varibles import *

def server_windows():
    global sock, client, groups, sock
    global start, PasswordCode
    if start:
        while 1:
            try:
                data, addres = sock.recvfrom(1024)
                text_utf = data.decode('utf-8')
                print(text_utf)
                if addres not in client:
                    client.append(addres) # Если такого клиента нету , то добавить

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






