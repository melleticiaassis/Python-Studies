lista_numeros = []
# Repete 5 vezes
for i in range(10):
    # pedir um valor ao usuario
    valor = float(input("Digite um número: "))
    lista_numeros.append(valor)
#[::-1] serve pra numerar o contrario 
print(lista_numeros[::-1])
