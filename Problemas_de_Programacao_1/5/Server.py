#Atividade 5 - Servidor
import socket

def classificar_nadador(idade):
    if 5 <= idade <= 7:
        return "Infantil A (5-7 anos)"
    elif 8 <= idade <= 10:
        return "Infantil B (8-10 anos)"
    elif 11 <= idade <= 13:
        return "Juvenil A (11-13 anos)"
    elif 14 <= idade <= 17:
        return "Juvenil B (14-17 anos)"
    elif idade >= 18:
        return "Adulto (18 anos ou mais)"
    else:
        return "Sem classificação para idade inferior a 5 anos"

def servidor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    print("Servidor pronto para receber conexões...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Conexão estabelecida com {addr}")

        data = conn.recv(1024).decode()
        if not data:
            break

        idade = int(data)

        classificacao = classificar_nadador(idade)

        conn.send(classificacao.encode())

        conn.close()

if __name__ == "__main__":
    servidor()
