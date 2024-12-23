import socket
import time
import signal
import sys
from datetime import datetime
import os
import json
import tkinter as tk


MIDDLEWARE_IP='127.0.0.1'
MIDDLEWARE_PORT=5000

cpu_sum = memory_sum = disk_sum = network_sum = counter = 0
uptime_first = uptime_last = None
start_time = None
last_resumes = []

def socket_test(socket_test): #testa se o socket continua aberto, enviando uma mensagem que n consome dados do buffer, apenas verifica se está aberto
    try:
        socket_test.send(b'', socket.MSG_PEEK)
        return True
    except (socket.error, BrokenPipeError):
        return False


def get_port_from_user(server_list):
    port_return = None  

    def submit():
        nonlocal port_return
        port_return = entry.get()  
        janela.destroy()  

    janela = tk.Tk()
    janela.title("Selecionar Porta")

    label = tk.Label(janela, text=f"Lista de Servidores:\n{server_list}", font=("Arial", 20))
    label.pack(pady=10)

    entry = tk.Entry(janela)
    entry.pack(pady=10)

    botao = tk.Button(janela, text="Confirmar", command=submit)
    botao.pack(pady=10)

    janela.mainloop()

    return port_return

def select_server(client_socket_select): # função pra selecionar a porta do servidor que vai ser acessado
    server_list = client_socket_select.recv(1024).decode('utf-8')
    print(server_list)
    port_return = input()
    client_socket_select.send(port_return.encode('utf-8'))

def start_connection(middleware_host, middleware_port):#inicia o socket com o middleware, passa a porta desejada e retorna o socket
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((middleware_host, middleware_port))
        server_list = client_socket.recv(1024).decode('utf-8')
        #fazer uma classe que o método chamado vai retornar a porta inserida
        
        print(server_list)
        port_return = get_port_from_user(server_list)
        client_socket.send(port_return.encode('utf-8'))
        print(client_socket.recv(1024).decode('utf-8'))
        return client_socket
    except Exception as e:
            print(f"Erro: {e}")



def save_history(resumes, filename='historico.json'):
    try:
        history = load_history(filename)
        history.extend(resumes)
        with open(filename, 'w') as file:
            json.dump(history, file, indent=4)
        print(f"Histórico salvo em {filename}")
    except Exception as e:
        print(f"Erro ao salvar o histórico: {e}")
    
def load_history(filename='historico.json'):
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Arquivo corrompido, iniciando com histórico vazio.")
    return []

def signal_handler(sig, frame):
    print("\nCliente parando...")
    save_history(last_resumes)
    sys.exit(0)

def parse_status(response_str):
    data = response_str.split(" | ")
    return {
        'cpu_usage': float(data[0].split(":")[1].replace("%", "").strip()),
        'memory_usage': float(data[1].split(":")[1].replace("%", "").strip()),
        'disk_usage': float(data[2].split(":")[1].replace("%", "").strip()),
        'network_status': data[3].split(":")[1].strip(),
        'uptime': float(data[4].split(":")[1].replace("horas", "").strip())
    }

def request_server_status(middleware_host='127.0.0.1', middleware_port=5000):
    global cpu_sum, memory_sum, disk_sum, network_sum, counter, start_time, last_resumes, uptime_first, uptime_last
    signal.signal(signal.SIGINT, signal_handler)
    
    start_time = datetime.now()
    print("----------------------------------------------------------------------------")
    print(f"Cliente iniciado às: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("----------------------------------------------------------------------------")

    client_socket = start_connection(MIDDLEWARE_IP, MIDDLEWARE_PORT)

    while socket_test(client_socket):
        try:
            client_socket.send(b"status")

            response = client_socket.recv(1024)

            response_str = response.decode('utf-8')

            print("Atualização em tempo real")
            print(f"Status do servidor: {response_str}")

            status_data = parse_status(response_str)
            cpu_sum += status_data['cpu_usage']
            memory_sum += status_data['memory_usage']
            disk_sum += status_data['disk_usage']
            network_sum += 1 if status_data['network_status'].lower() == "ativo" else 0
            
            if uptime_first is None:
                uptime_first = status_data['uptime']
            uptime_last = status_data['uptime']
            counter += 1

            if counter == 10:
                os.system('cls' if os.name == 'nt' else 'clear')
                avg_cpu = cpu_sum / 10
                avg_memory = memory_sum / 10
                avg_disk = disk_sum / 10
                total_time = datetime.now() - start_time

                resume = {
                    "data_hora": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "avg_cpu": avg_cpu,
                    "avg_memory": avg_memory,
                    "avg_disk": avg_disk,
                    "total_time": str(total_time).split('.')[0]
                }
                
                last_resumes.append(resume)
                print("\nResumo das últimas 10 execuções:")
                for r in last_resumes:
                    print(f"\nData e Hora: {r['data_hora']}")
                    print(f"Média de Uso de CPU: {r['avg_cpu']:.2f}%")
                    print(f"Média de Uso de Memória: {r['avg_memory']:.2f}%")
                    print(f"Média de Uso de Disco: {r['avg_disk']:.2f}%")
                    print(f"Tempo total de atividade: {r['total_time']}")
                
                cpu_sum = memory_sum = disk_sum = network_sum = counter = 0

            #client_socket.close()
        except Exception as e:
            print(f"Erro: {e}")
            client_socket.close()
        time.sleep(1)


if __name__ == "__main__":
    request_server_status()

