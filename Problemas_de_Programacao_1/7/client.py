import socket

def main():
    # Criar socket
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(('localhost', 12345))

    idade = int(input("Digite a idade do funcionário: "))
    tempo_servico = int(input("Digite o tempo de serviço (em anos): "))
    
    # Enviar dados para o servidor
    cliente_socket.sendall(f"{idade},{tempo_servico}".encode('utf-8'))

    # Receber a resposta do servidor
    resposta = cliente_socket.recv(1024).decode('utf-8')
    print(resposta)

    cliente_socket.close()

if __name__ == "__main__":
    main()