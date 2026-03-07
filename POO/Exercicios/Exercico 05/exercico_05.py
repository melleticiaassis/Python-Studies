class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total
class Cliente:
    def __init__(self, nome):
        self.nome = nome
p1 = Produto("Notebook", 3000)
p2 = Produto("Mouse", 100)

cliente = Cliente("João")

carrinho = Carrinho()
carrinho.adicionar_produto(p1)
carrinho.adicionar_produto(p2)

print(cliente.nome)
print("Total:", carrinho.total())


