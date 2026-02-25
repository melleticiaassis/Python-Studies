def senha_valida(senha):
    if not isinstance(senha, str):
        raise TypeError("Senha deve ser uma string")

    if len(senha) < 8:
        return False

    tem_numero = any(char.isdigit() for char in senha)

    return tem_numero
