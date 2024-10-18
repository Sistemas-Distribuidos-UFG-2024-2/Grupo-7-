import socket
from utils.calculo import calcular_salario_liquido  # Importando a função

def servidor():
    # Configurando o servidor
    host = 'localhost'
    porta = 12345
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, porta))
    servidor_socket.listen(1)

    print("Servidor pronto e aguardando conexões...")

    while True:
        # Aceitando a conexão do cliente
        conn, addr = servidor_socket.accept()
        print(f"Conectado por {addr}")

        # Recebendo dados do cliente
        dados = conn.recv(1024).decode()

        if not dados:
            break

        # Extraindo os dados do cliente
        nome, nivel, salario_bruto, dependentes = dados.split(',')
        salario_bruto = float(salario_bruto)
        dependentes = int(dependentes)

        # Calculando o salário líquido
        resultado = calcular_salario_liquido(nome, nivel, salario_bruto, dependentes)

        # Enviando o resultado de volta ao cliente
        conn.send(resultado.encode())

        # Fechando a conexão com o cliente
        conn.close()

if __name__ == "__main__":
    servidor()
