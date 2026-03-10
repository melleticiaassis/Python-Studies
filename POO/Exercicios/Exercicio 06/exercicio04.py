# Sistema de Produtos.

class Produto:

    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, quantidade):
        if quantidade > self.estoque:
            print("Estoque insuficiente")
        else:
            self.estoque -= quantidade
            print("Venda realizada")

    def adicionar_estoque(self, quantidade):
        self.estoque += quantidade

    def mostrar_estoque(self):
        print(self.estoque)
        
p1 = Produto( "mouse", 1200 , 100 )       
p1.vender(2)
p1.mostrar_estoque()
        
        