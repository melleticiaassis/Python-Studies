# Declaração de Classe
class Construcao:
    def __init__(self): # Métado Construtor
        # Atributo de Instância
        self.nome = " "
        self.idade = 0 
# Métado de Instância
    def aniversario(self):
        self.idade += 1 
    def mensagem(self):
        return f"{self.nome} é Construtor(a) e tem {self.idade} anos de idade "
    
# Declaração de Objetos
g1 = Construcao() # É uma variavel evoluida no caso a classe
g1.nome = "Aurora" # são atributos pois *não tem () no final*
g1.idade = 20
g1.aniversario() # É um métado pois *tem () no final*
print(g1.mensagem())

g2 = Construcao()
g2.nome = "Alessandro"
g2.idade = 25
g2.aniversario()
print(g2.mensagem())

g3 = Construcao()
print(g3.mensagem)