# Exercico teste de Try e Except

try:
    numerador = int(input("Numerador: "))
    denominador = int(input("Denominador: "))
    valor = numerador / denominador
#    forma genérica 
# except Exception as erro:
#     print(f"Problema encontrado foi {erro.__class__}")

except (ValueError , TypeError):
    print("Tivemos um problema com o valor digitado")
else:
    print(f"O resultado é {valor:.1f}")
finally:
    print("Volte sempre ;)")