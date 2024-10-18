#Atividade 3 - Servidor
import socket

def verificar_aprovacao(n1, n2, n3):
    m = (n1 + n2) / 2

    if m >= 7.0:
        return "Aprovado com média: {:.2f}".format(m)
    elif m > 3.0:
        m_final = (m + n3) / 2
        if m_final >= 5.0:
            return "Aprovado com média final (Utilizando N3): {:.2f}".format(m_final)
        else:
            return "Reprovado com média final (Utilizando N3): {:.2f}".format(m_final)
    else:
        return "Reprovado com média: {:.2f}".format(m)

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

        n1, n2, n3 = map(float, data.split(','))

        resultado = verificar_aprovacao(n1, n2, n3)


        conn.send(resultado.encode())

        conn.close()

if __name__ == "__main__":
    servidor()
