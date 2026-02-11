# Calcula a média das notas

notas = []
for i in range(4):
    numero = float(input("Digite sua média: "))
    notas.append(numero)
media = sum(notas) / len(notas)
# sun -> soma os números 
# len -> conta cada valor digitado
print(f"Notas: {notas}")
