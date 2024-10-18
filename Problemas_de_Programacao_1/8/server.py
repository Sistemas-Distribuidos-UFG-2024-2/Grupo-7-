import socket

def calcular_credito(saldo_medio):
    if saldo_medio <= 200:
        return 0
    elif 201 <= saldo_medio <= 400:
        return saldo_medio * 0.20
    elif 401 <= saldo_medio <= 600:
        return saldo_medio * 0.30
    else:  # saldo_medio > 600
        return saldo_medio * 0.40

def main():
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind(('localhost', 12345))
    servidor_socket.listen(1)

    print("Servidor aguardando conexões...")
    while True:
        conexao, endereco = servidor_socket.accept()
        print(f"Conexão estabelecida com {endereco}")

        dados = conexao.recv(1024).decode('utf-8')
        saldo_medio = float(dados)

        credito = calcular_credito(saldo_medio)
        resposta = f"Saldo médio: R$ {saldo_medio:.2f}, Valor do crédito: R$ {credito:.2f}"

        conexao.sendall(resposta.encode('utf-8'))
        conexao.close()

if __name__ == "__main__":
    main()