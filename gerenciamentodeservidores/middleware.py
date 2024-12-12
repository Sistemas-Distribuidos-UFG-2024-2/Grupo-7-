import threading
import queue
import socket
import threading
import signal
import sys
import pickle #usado para serialização do set para envio ao health checker
import time

running = True  
list_servers = set()
#last_updade = set()

SERVER_LIST_IP = "127.0.0.1"
SERVER_LIST_PORT = 4999

HEALTH_CHECKER_IP = "127.0.0.1"
HEALTH_CHECKER_PORT = 4998

def update(last_update):
    list_servers.clear()
    for server in last_update:
        list_servers.add(server)
    

def health_checker_connection ():
    try:
        health_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        health_socket.bind((HEALTH_CHECKER_IP, HEALTH_CHECKER_PORT))
        health_socket.listen(5)

        health_connection, addr = health_socket.accept()

        print(f"Health Checker conectado - {addr}")
        
        while socket_test(health_connection):
            servers_send = pickle.dumps(list_servers) #serializa o set para enviar al health_checker
            health_connection.sendall(servers_send)
            servers_on = set()
            servers_on_set = health_connection.recv(1024)
            last_update = pickle.loads(servers_on_set)
            print(f"Servidores Online:\n{last_update}")
            update(last_update)
            time.sleep(2)
    except Exception as e:
        print(f"Erro ao se comunicar com o Health_checker: {e}")

def client_server_select(client_socket): #melhorar isso aqui
    client_socket.send((create_string_servers()+"\nSelecione o número de uma porta:").encode('utf-8'))
    port = 0
    port = client_socket.recv(1024).decode('utf-8')
    #fazer verificação da porta e terminar essa bagaça
    print(port)
    client_socket.send("Porta OK".encode('utf-8'))
    return int(port)

def socket_test(socket_test): #testa se o socket continua aberto, enviando uma mensagem que n consome dados do buffer, apenas verifica se está aberto
    try:
        socket_test.send(b'', socket.MSG_PEEK)
        return True
    except (socket.error, BrokenPipeError):
        return False

def server_list(host, port):# tem como objetivo abrir um socket para escutar os servidores que querem anunciar seus endereços
    while True:
        try:
            print("Escutando anúncio dos servidores...")
            list_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            list_socket.bind((host,port))
            list_socket.listen(5) 
            conn, addr = list_socket.accept()
            list_connect= conn
            server = list_connect.recv(1024).decode('utf-8')
            print(f"Servidor {server} adicionado")
            list_servers.add(server)
            print(create_string_servers())            

            list_connect.close()
            list_socket.close()
        except Exception as e:
            print(f"Erro {e} encontrado")
        finally:
            if list_connect:
                try:
                    list_connect.close()
                except Exception as e:
                    print(f"Erro ao fechar a list_connect: {e}")
            if list_socket:
                try:
                    list_socket.close()
                except Exception as e:
                    print(f"Erro ao fechar list_socket: {e}")

def create_string_servers():# cria string com os servidores disponíveis
    list = "----------------------------------------------------------------------------\nServidores Disponiveis:"
    for server in list_servers:
        list += "\n" + server
    list += "\n----------------------------------------------------------------------------"
    return list

def handle_client(client_socket, server_host='127.0.0.1', server_port=0):
    try:
        server_list_to_send = create_string_servers()
        while(server_port==0):
            server_port = client_server_select(client_socket)
            print(server_port)
        
        #client_socket.send(server_list_to_send.encode('utf-8'))
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect((server_host, server_port))
        while socket_test(server_socket) and socket_test(client_socket):
            print("Conexão com o servidor bem-sucedida para solicitar o status.")
            
            server_socket.send(b"status")
            
            response = server_socket.recv(1024)
            
            client_socket.send(response)
            print("Resposta enviada com sucesso ao cliente com o status do servidor.")

        server_socket.close()
        client_socket.close()
    except Exception as e:
        print(f"Erro ao processar o cliente: {e}")
        client_socket.close()

def start_middleware(host='127.0.0.1', port=5000):
    global running
    middleware = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    middleware.bind((host, port))
    
    #thread pra escutar o anúncio dos servidores
    thread_listener = threading.Thread(target=server_list,args=(SERVER_LIST_IP,SERVER_LIST_PORT))
    thread_listener.start()
    
    thread_health_checker = threading.Thread(target=health_checker_connection,args=())
    thread_health_checker.start()

    middleware.listen(5)
    middleware.settimeout(1)  
    print(f"Middleware iniciado com sucesso e ouvindo em {host}:{port}")

    def signal_handler(sig, frame):
        global running
        print("Desligando o middleware...")
        running = False
    signal.signal(signal.SIGINT, signal_handler)  

    
    while running:
        try:
            client_socket, addr = middleware.accept()
            print(f"Conexão bem-sucedida com o cliente de {addr}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
        except socket.timeout:
            continue  

    middleware.close()
    print("Middleware desligado.")

if __name__ == "__main__":
    start_middleware()
