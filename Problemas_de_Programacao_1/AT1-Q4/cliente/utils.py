def validar_entrada(altura, sexo):
    try:
        altura = float(altura)
        if sexo not in ('M', 'F'):
            raise ValueError("Sexo inválido. Use 'M' para masculino ou 'F' para feminino.")
        return True
    except ValueError as e:
        print(f"Erro: {e}")
        return False
