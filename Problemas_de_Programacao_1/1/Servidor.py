#Atividade 1 - Servidor
import socket

def calcular_reajuste(cargo, salario):
    if cargo.lower() == "operador":
        return salario * 1.20
    elif cargo.lower() == "programador":
        return salario * 1.18
    else:
        return salario  

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

        nome, cargo, salario = data.split(',')
        salario = float(salario)

        salario_reajustado = calcular_reajuste(cargo, salario)
        resultado = f"Nome: {nome}, Salário reajustado: {salario_reajustado:.2f}"

        conn.send(resultado.encode())

        conn.close()

if __name__ == "__main__":
    servidor()
