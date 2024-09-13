import socket

def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)
    print(f"Servidor 1 ouvindo na porta {port}...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Conexão estabelecida com {addr}")
        message = conn.recv(1024).decode()
        print(f"Mensagem recebida: {message}")
        if message == "Hello":
            conn.sendall("World".encode())
        conn.close()

if __name__ == "__main__":
    start_server(5001)
