# class Carrinho:
#     def __init__(self):
#         self.produtos = []
#         self.produtos.append("Notebook")

#     def add_produto(self, produto):
#         self.produtos.append(produto)


# carrinho = Carrinho()
# carrinho.add_produto("Produto1")

# print(carrinho.produtos)


class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto):
        self.itens.append(produto)

    def remover_produto(self, produto):
        self.itens.remove(produto)

    def calcular_total(self):
        total = 0
        for produto in self.itens:
            total += produto.preco
        return total