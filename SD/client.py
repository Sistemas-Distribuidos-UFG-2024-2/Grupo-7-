import socket

def connect_to_server(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendall("Hello".encode())
    response = client_socket.recv(1024).decode()
    print(f"Resposta do servidor {port}: {response}")
    client_socket.close()

if __name__ == "__main__":
    host = 'localhost'
    ports = [5001, 5002, 5003]

    for port in ports:
        connect_to_server(host, port)
