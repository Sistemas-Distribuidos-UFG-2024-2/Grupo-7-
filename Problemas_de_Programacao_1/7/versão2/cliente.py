import rpyc

def main():
    conn = rpyc.connect('localhost', 12345)

    idade = int(input("Digite a idade do funcionário: "))
    tempo_servico = int(input("Digite o tempo de serviço (em anos): "))
    
    # Chamar o método remoto
    pode_aposentar = conn.root.pode_aposentar(idade, tempo_servico)

    if pode_aposentar:
        print("O funcionário pode se aposentar.")
    else:
        print("O funcionário não pode se aposentar.")

    conn.close()

if __name__ == "__main__":
    main()