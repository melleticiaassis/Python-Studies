class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def reduzir_estoque(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
        else:
            print("Estoque insuficiente!")


p1 = Produto("Notebook", 3503, 58)
print(p1.nome)
print(p1.preco)
print(p1.estoque)

p1.reduzir_estoque(2)

print(p1.estoque)