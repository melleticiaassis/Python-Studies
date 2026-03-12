class Pedido:
    def __init__(self, cliente, carrinho):
        self.cliente = cliente
        self.carrinho = carrinho
        self.total = carrinho.calcular_total()
        