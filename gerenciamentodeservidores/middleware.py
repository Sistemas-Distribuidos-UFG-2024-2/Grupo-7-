import threading
import queue
import socket
import threading
import signal
import sys

running = True  
list_servers = []

def server_list(host, port):
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
            
            list_servers.append(server)#armazena servidor na lista
            
            for s in list_servers:
                print(s)
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


def handle_client(client_socket, server_host='127.0.0.1', server_port=5001):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect((server_host, server_port))
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
    
    thread_listener = threading.Thread(target=server_list,args=("127.0.0.1",4999))
    thread_listener.start()
    
    #server_list("121.0.0.1", 4999)


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
