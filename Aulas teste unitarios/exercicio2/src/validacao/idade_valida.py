# def validar_idade(idade):
#     if idade < 0:
#         raise ValueError("Idade inválida")
#     return idade >= 18

def validar_idade(idade: int) -> bool:
    if idade < 0:
        raise ValueError("Idade inválida")
    return idade >= 18