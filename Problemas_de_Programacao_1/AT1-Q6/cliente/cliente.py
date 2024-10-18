import socket

def cliente():
    # Coleta de dados do funcionário
    nome = input("Informe o nome do funcionário: ")
    nivel = input("Informe o nível do funcionário (A, B, C, D): ").upper()
    salario_bruto = float(input("Informe o salário bruto: "))
    dependentes = int(input("Informe o número de dependentes: "))

    # Preparando dados para enviar ao servidor
    dados = f"{nome},{nivel},{salario_bruto},{dependentes}"

    # Configurando conexão com o servidor
    host = 'localhost'
    porta = 12345

    # Criando socket
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((host, porta))

    # Enviando dados para o servidor
    cliente_socket.send(dados.encode())

    # Recebendo resposta do servidor
    resultado = cliente_socket.recv(1024).decode()

    print("Resultado do servidor:", resultado)

    # Fechando a conexão
    cliente_socket.close()

if __name__ == "__main__":
    cliente()
