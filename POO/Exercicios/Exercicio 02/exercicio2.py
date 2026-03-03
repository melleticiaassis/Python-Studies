# Declaração de Classe
class Usuario:
    
    """
    Essa classe cria um Usuario, que é uma pessoa que tem nome e idade.
    Para criar uma nova pessoa, use
    variavel = Usuario(nome, idade)
    """
    def __init__(self, nome = "", idade = 0): # Métado Construtor
        # Atributo de Instância
        self.nome = nome
        self.idade = idade
# Métado de Instância
    def aniversario(self):
        self.idade += 1 
    def mensagem(self):
        return f"{self.nome} é Construtor(a) e tem {self.idade} anos de idade "
    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"
    
# Declaração de Objetos
g1 = Usuario(nome = "Aurora", idade = 20) 
g1.aniversario() 
print(g1.mensagem())
print(g1.__dict__)
print(g1.__getstate__)
print(g1.__class__)



# É uma variavel evoluida no caso a classe
# Atributos é os que *não tem () no final*
# Métado é os que *tem () no final*

# print(g1.__doc__) #Douder Attridute
