import socket

def cliente():
    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo do funcionário (operador ou programador): ")
    salario = float(input("Digite o salário do funcionário: "))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    dados = f"{nome},{cargo},{salario}"
    client_socket.send(dados.encode())

    resultado = client_socket.recv(1024).decode()
    print("Resposta do servidor:", resultado)

    client_socket.close()

if __name__ == "__main__":
    cliente()
