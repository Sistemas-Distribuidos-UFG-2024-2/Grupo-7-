import socket
from utils import calcular_peso_ideal
import logging

logging.basicConfig(filename='logs/log.txt', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def main():
    # Configurações do servidor
    host = 'localhost'
    port = 12345

    # Criar socket do servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Servidor aguardando conexão...")

    while True:
        conn, addr = server_socket.accept()
        logging.info(f"Conectado por {addr}")
        print(f"Conectado por {addr}")

        try:
            # Receber dados do cliente
            dados = conn.recv(1024).decode('utf-8')
            altura, sexo = dados.split(',')
            altura = float(altura)

            # Calcular peso ideal
            peso_ideal = calcular_peso_ideal(altura, sexo)

            # Enviar o resultado de volta ao cliente
            conn.sendall(str(peso_ideal).encode('utf-8'))

        except Exception as e:
            logging.error(f"Erro durante a conexão: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    main()
