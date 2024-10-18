import socket
from servidor.utils import verificar_maioridade

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Servidor aguardando conexão...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Conectado por {addr}")

        data = conn.recv(1024).decode()
        if not data:
            break

        nome, sexo, idade = data.split(',')
        result = verificar_maioridade(nome, sexo, idade)

        conn.sendall(result.encode())
        conn.close()

if __name__ == '__main__':
    main()
