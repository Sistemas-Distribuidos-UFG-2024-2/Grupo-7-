import socket

def main():
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(('localhost', 12345))

    try:
        saldo_medio = float(input("Digite o saldo médio do cliente: "))
        if saldo_medio < 0:
            print("O saldo médio não pode ser negativo.")
            cliente_socket.close()
            return
        
        # Enviar saldo médio para o servidor
        cliente_socket.sendall(str(saldo_medio).encode('utf-8'))

        # Receber a resposta do servidor
        resposta = cliente_socket.recv(1024).decode('utf-8')
        print(resposta)

    except ValueError:
        print("Por favor, insira um valor numérico válido.")
    finally:
        cliente_socket.close()

if __name__ == "__main__":
    main()