import socket
import psutil
import threading
import time
import signal
import sys

running = True  

#testa o valor passado pra porta e verifica se os 3 acima e abaixo estão disponíveis. 
def pick_free_port_number():
    number_port = int(input("Escolha uma porta para seu servidor\nRecomendamos valores acima de 5000\n:"))#Ainda não tem integração direta com o middlware. Ele sempre espera um servidor com porta 5001
    host='127.0.0.1'
    if (port_test(host, number_port)):
        for port in range(number_port-3,number_port+3):
            if (port_test(host,port)==False):
                print(f"Sua porta não está livre para uso.\nPorém, a porta {port} está.")
                break
        return 0
    else:
        return number_port
                
#testa se a porta ta livre
def port_test(host,port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((host, port))
            return False #porta livre
        except socket.error:
            return True  #porta em uso


def handle_client(client_socket):
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
    #port_test("121.0.0.1", port)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    server.settimeout(1)  
    print(f"Servidor iniciado com sucesso e ouvindo em {host}:{port}")

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
