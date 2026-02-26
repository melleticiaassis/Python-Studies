
def calcular_desconto(preco: float, porcentagem: float) -> float:

    # Valida se o preço é negativo
    if preco < 0:
        raise ValueError("O preço não pode ser negativo.")

    # Valida se a porcentagem está fora do intervalo permitido
    if porcentagem < 0 or porcentagem > 100:
        raise ValueError("A porcentagem deve estar entre 0 e 100.")

    # Calcula o preço final aplicando o desconto diretamente
    preco_final = preco * (1 - porcentagem / 100)

    # Retorna o valor arredondado para 2 casas decimais
    return round(preco_final, 2)