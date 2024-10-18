import socket

def pode_aposentar(idade, tempo_servico):
    if idade >= 65 and tempo_servico >= 30:
        return True
    elif idade >= 60 and tempo_servico >= 25:
        return True
    return False

def main():
    # Criar socket
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind(('localhost', 12345))
    servidor_socket.listen(1)

    print("Servidor aguardando conexões...")
    while True:
        conexao, endereco = servidor_socket.accept()
        print(f"Conexão estabelecida com {endereco}")

        dados = conexao.recv(1024).decode('utf-8')
        idade, tempo_servico = map(int, dados.split(','))

        if pode_aposentar(idade, tempo_servico):
            resposta = "O funcionário pode se aposentar."
        else:
            resposta = "O funcionário não pode se aposentar."

        conexao.sendall(resposta.encode('utf-8'))
        conexao.close()

if __name__ == "__main__":
    main()