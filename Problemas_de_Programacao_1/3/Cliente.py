#Atividade 3 - Cliente
import socket

def cliente():
    n1 = float(input("Digite a N1: "))
    n2 = float(input("Digite a N2: "))
    n3 = float(input("Digite a N3: "))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    dados = f"{n1},{n2},{n3}"
    client_socket.send(dados.encode())

    resultado = client_socket.recv(1024).decode()
    print("Resposta do servidor:", resultado)

    client_socket.close()

if __name__ == "__main__":
    cliente()
