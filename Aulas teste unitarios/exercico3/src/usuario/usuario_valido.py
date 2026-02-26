def validar_usuario(nome, idade):
    if not nome:
        raise ValueError("Preencha o campo, não pode estra vazio")
    if idade < 0:
        raise ValueError("Idade inválida, preencha o campo!")
    if idade < 18:
        return "menor"
    return "maior"