def calcular_salario_liquido(nome, nivel, salario_bruto, dependentes):
    # Calculando o desconto com base no nível e número de dependentes
    if nivel == 'A':
        desconto = 0.03 if dependentes == 0 else 0.08
    elif nivel == 'B':
        desconto = 0.05 if dependentes == 0 else 0.10
    elif nivel == 'C':
        desconto = 0.08 if dependentes == 0 else 0.15
    elif nivel == 'D':
        desconto = 0.10 if dependentes == 0 else 0.17
    else:
        return "Nível inválido"

    salario_liquido = salario_bruto * (1 - desconto)
    
    return f"Nome: {nome}, Nível: {nivel}, Salário Líquido: R$ {salario_liquido:.2f}"
