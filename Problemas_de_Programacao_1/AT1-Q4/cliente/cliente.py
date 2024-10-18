import socket

def main():
    # Coleta de dados
    altura = input("Digite a altura da pessoa (em metros): ")
    sexo = input("Digite o sexo da pessoa (M para masculino, F para feminino): ")

    # Configurações do cliente
    host = 'localhost'
    port = 12345

    # Criar socket do cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        # Enviar dados para o servidor
        dados = f"{altura},{sexo}"
        client_socket.sendall(dados.encode('utf-8'))

        # Receber o resultado do servidor
        peso_ideal = client_socket.recv(1024).decode('utf-8')
        print(f"O peso ideal é: {peso_ideal}")

    finally:
        # Fechar a conexão
        client_socket.close()

if __name__ == "__main__":
    main()
