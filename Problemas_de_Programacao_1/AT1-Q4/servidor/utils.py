def calcular_peso_ideal(altura, sexo):
    if sexo == 'M':
        return (72.7 * altura) - 58
    elif sexo == 'F':
        return (62.1 * altura) - 44.7
    else:
        return None
