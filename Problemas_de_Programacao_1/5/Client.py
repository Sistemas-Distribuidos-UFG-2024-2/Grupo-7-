#Atividade 5 - Cliente
import socket

def cliente():
    idade = int(input("Digite a idade do nadador: "))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    client_socket.send(str(idade).encode())

    classificacao = client_socket.recv(1024).decode()
    print("Classificação do nadador:", classificacao)

    client_socket.close()

if __name__ == "__main__":
    cliente()

