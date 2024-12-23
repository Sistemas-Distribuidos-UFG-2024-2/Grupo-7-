import requests
import socket
import signal
import pickle
import time

HEALTH_CHECKER_IP = "127.0.0.1"
HEALTH_CHECKER_PORT = 4998

servers_to_test = set()
servers_on = set()

def socket_test(socket_test): #testa se o socket continua aberto, enviando uma mensagem que n consome dados do buffer, apenas verifica se está aberto
    try:
        socket_test.send(b'', socket.MSG_PEEK)
        return True
    except (socket.error, BrokenPipeError):
        return False


def check_server_health(servers): #verifica a saúde dos servidores e retorna apenas os onlines. 
    try:
        servers_list = list(servers)
        to_return = set()
        for server in servers_list:
            socket_test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_test.settimeout(2)
            host = server.split(":")
            result = socket_test.connect_ex((host[0],int(host[1])))

            if result==0:
                print("Porta aberta")
                to_return.add(server)
            else:
                print("Porta fechada")
            
        return to_return
    except Exception as e:
        print(f"Não foi possível realizar a verificação dos servidores devido ao erro {e}")
        return servers


def start_health_checker():
    health_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Health Checker iniciado com sucesso")

    def signal_handler(sig, frame):
        global running
        print("Desligando o Health Checker...")
        running = False
    signal.signal(signal.SIGINT, signal_handler)  

    try:
        health_socket.connect((HEALTH_CHECKER_IP,HEALTH_CHECKER_PORT))
        print(f"Conexão com Middleware estabelecida")     
    except Exception as e:
        print(f"Erro ao conectar com o Middleware: {e}")

    while socket_test(health_socket):
        to_convert = health_socket.recv(1024)
        if to_convert:
            servers_to_test = pickle.loads(to_convert)
            print(servers_to_test) 
        servers_on = check_server_health(servers_to_test)
        to_send = pickle.dumps(servers_on)
        health_socket.sendall(to_send)
        time.sleep(2)
        
if __name__ == "__main__":
    start_health_checker()


