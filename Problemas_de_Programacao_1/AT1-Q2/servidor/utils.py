def verificar_maioridade(nome, sexo, idade):
    idade = int(idade)
    if sexo.upper() == 'M':
        maioridade = 18
    elif sexo.upper() == 'F':
        maioridade = 21
    else:
        return f"Sexo inválido para {nome}"

    if idade >= maioridade:
        return f"{nome} já atingiu a maioridade."
    else:
        return f"{nome} ainda não atingiu a maioridade."
