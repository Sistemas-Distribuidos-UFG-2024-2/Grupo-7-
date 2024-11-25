    

import socket


while True:
    print("Thread server list iniciado")
    list_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    list_socket.bind(("127.0.0.1", 4999))
    list_socket.listen(5) 
    list_connect, addr = list_socket.accept()
    server = list_connect.recv(1024)
    print(server)
    list_connect.close()
    list_socket.close()