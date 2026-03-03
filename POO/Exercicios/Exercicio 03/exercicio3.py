# Cria uma conta báncaria e permite fazer saques e depósitos
class ContaBancaria:
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}.")
        
    print("Olá prezado(a)!")
    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."
    
    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito no valor R${valor:,.2f} autorizado na conta {self.id}. ")
        
    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque negado de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE!")
        else:
            self.saldo -= valor
            print(f"Saque no valor R${valor:,.2f} autorizado na conta {self.id}. ")

c1 = ContaBancaria(id=2527, nome="Helena", saldo=7000)
c1.deposito(700)
c1.sacar(10000000)
print(c1)