# criamos uma lista vazia para guardar as consoantes
consoantes = []

# loop para ler 10 letras do usuário
for i in range(10):
    # lê a letra e transforma em minúscula para facilitar a comparação
    letra = input("Digite uma letra: ").lower()
    
    # werifica se é letra e se não é vogal
    # se for uma letra (isalpha() = True) e não estiver em "aeiou" → é consoante
    if letra.isalpha() and letra not in "aeiou":
        # adiciona a consoante na lista
        consoantes.append(letra)

# imprime todas as consoantes e a quantidade de consoantes lidas
print(f"Consoantes: {consoantes} - Quantidade: {len(consoantes)}")
