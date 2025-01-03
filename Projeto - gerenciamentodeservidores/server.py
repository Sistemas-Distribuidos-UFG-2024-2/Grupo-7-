import socket
import psutil
import threading
import time
import signal
import sys

running = True  

def announcement_server(host_server,port_server,host,port):
    try:
        announcement_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        announcement_socket.connect((host_server,port_server))
        to_send = str(host)+":"+str(port)
        announcement_socket.send(to_send.encode('utf-8'))
        announcement_socket.close()
        print("Anúncio realizado com sucesso")
    except Exception as e:
        print(f"Exceção encontrada ao anunciar endereço: {e}")
        announcement_socket.close()
    
def pick_free_port_number(): #testa o valor passado pra porta e verifica se os 3 acima e abaixo estão disponíveis.
    number_port = int(input("Escolha uma porta para seu servidor\nRecomendamos valores acima de 5000: "))
    host='127.0.0.1'
    if (port_test(host, number_port)):
        for port in range(number_port-3,number_port+3):
            if (port_test(host,port)==False):
                print(f"Sua porta não está livre para uso.\nPorém, a porta {port} está.\n")
                break
        return 0
    else:
        return number_port
                
def port_test(host,port): #testa se a porta ta livre
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((host, port))
            return False #porta livre
        except socket.error:
            return True  #porta em uso

def socket_test(socket_test): #testa se o socket continua aberto, enviando uma mensagem que n consome dados do buffer, apenas verifica se está aberto
    try:
        socket_test.send(b'', socket.MSG_PEEK)
        return True
    except (socket.error, BrokenPipeError):
        return False

def handle_client(client_socket):
    while socket_test(client_socket):
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        network_status = "Inativo"
        for interface, stats in psutil.net_if_stats().items():
            if stats.isup:
                network_status = "Ativo"
                break

        uptime = time.time() - psutil.boot_time()

        response = (
            f"Uso de CPU: {cpu_usage}% | "
            f"Uso de Memória: {memory_info}% | "
            f"Uso de Disco: {disk_usage}% | "
            f"Status da Rede: {network_status} | "
            f"Tempo de Atividade: {uptime / 3600:.2f} horas"
        )

        client_socket.send(response.encode('utf-8'))
        print("Resposta enviada com sucesso ao cliente com o status do servidor.")
    client_socket.close()

def start_server(host='127.0.0.1'):
    global running
    port = 0
    while port==0:
        port = pick_free_port_number()
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))


    server.listen(5)
    server.settimeout(1)  
    print(f"Servidor iniciado com sucesso e ouvindo em {host}:{port}")

    announcement_server("127.0.0.1",4999,host,port)

    def signal_handler(sig, frame):
        global running
        print("Desligando o servidor...")
        running = False

    signal.signal(signal.SIGINT, signal_handler)

    while running:
        try:
            client_socket, addr = server.accept()
            print(f"Conexão bem-sucedida com o cliente de {addr}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
        except socket.timeout:
            continue  

    server.close()
    print("Servidor desligado.")

if __name__ == "__main__":
    start_server()
