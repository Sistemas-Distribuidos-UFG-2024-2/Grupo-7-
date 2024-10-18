import socket
from cliente.utils import formata_dados

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    nome = input("Digite o nome: ")
    sexo = input("Digite o sexo (M/F): ")
    idade = input("Digite a idade: ")

    dados = formata_dados(nome, sexo, idade)
    client_socket.sendall(dados.encode())

    result = client_socket.recv(1024).decode()
    print(result)

    client_socket.close()

if __name__ == '__main__':
    main()
