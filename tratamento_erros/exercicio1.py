def leiaInt():
    while True:
        try:
            return int(input("Digite um número inteiro: "))
        except ValueError:
            print("Erro! Digite um número inteiro válido.")


def leiaFloat():
    while True:
        try:
            return float(input("Digite um número real: "))
        except ValueError:
            print("Erro! Digite um número real válido.")


# Chamando as funções (ESSA PARTE FALTAVA)
n = leiaInt()
f = leiaFloat()

print(f"Você digitou o inteiro: {n}")
print(f"Você digitou o float: {f}")
