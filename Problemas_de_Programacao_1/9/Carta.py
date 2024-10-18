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