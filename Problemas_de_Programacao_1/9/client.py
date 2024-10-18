import socket

def main():
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(('localhost', 12345))

    # Receber a resposta do servidor
    resposta = cliente_socket.recv(1024).decode('utf-8')
    print("Cartas recebidas do servidor:")
    print(resposta)

    cliente_socket.close()

if __name__ == "__main__":
    main()