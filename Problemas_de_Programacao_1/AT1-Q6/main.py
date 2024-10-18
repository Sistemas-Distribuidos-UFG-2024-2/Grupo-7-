import subprocess

def main():
    # Inicia o servidor
    subprocess.Popen(['python', 'servidor/servidor.py'])
    
    # Aguardar o servidor inicializar
    input("Pressione Enter para iniciar o cliente...")
    
    # Inicia o cliente
    subprocess.run(['python', 'cliente/cliente.py'])

if __name__ == "__main__":
    main()
