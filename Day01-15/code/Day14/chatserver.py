from socket import socket
from threading import Thread


def main():

    class ClientHandler(Thread):

        def __init__(self, client):
            super().__init__()
            self._client = client

        def run(self):
            try:
                while True:
                    try:
                        data = self._client.recv(1024)
                        if data.decode('utf-8') == 'byebye':
                            clients.remove(self._client)
                            self._client.close()
                            break
                        else:
                            for client in clients:
                                client.send(data)
                    except Exception as e:
                        print(e)
                        clients.remove(self._client)
                        break
            except Exception as e:
                print(e)

    server = socket()
    server.bind(('10.7.189.118', 12345))
    server.listen(512)
    clients = []
    while True:
        curr_client, addr = server.accept()
        print(addr[0], '连接到服务器.')
        clients.append(curr_client)
        ClientHandler(curr_client).start()


if __name__ == '__main__':
    main()
