import socket

class Carta:
    valores = {
        1: "ás",
        2: "dois",
        3: "três",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove",
        10: "dez",
        11: "valete",
        12: "dama",
        13: "rei"
    }

    naipes = {
        1: "ouros",
        2: "paus",
        3: "copas",
        4: "espadas"
    }

    def __init__(self, valor, naipe):
        if valor < 1 or valor > 13 or naipe < 1 or naipe > 4:
            raise ValueError("Valor ou naipe inválido.")
        self.valor = valor
        self.naipe = naipe

    def nome(self):
        return f"{self.valores[self.valor]} de {self.naipes[self.naipe]}"

def main():
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind(('localhost', 12345))
    servidor_socket.listen(1)

    print("Servidor aguardando conexões...")
    while True:
        conexao, endereco = servidor_socket.accept()
        print(f"Conexão estabelecida com {endereco}")

        # Criando algumas cartas
        cartas = [
            Carta(1, 2),  # ás de paus
            Carta(11, 1), # valete de ouros
            Carta(7, 4)   # sete de espadas
        ]

        # Preparando a resposta
        resposta = "\n".join(carta.nome() for carta in cartas)
        
        conexao.sendall(resposta.encode('utf-8'))
        conexao.close()

if __name__ == "__main__":
    main()