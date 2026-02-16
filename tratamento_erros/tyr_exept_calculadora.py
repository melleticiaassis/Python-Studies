# try -> se der erro na executar a operacao.
# except -> usado quando a execução falhar, dando uma mensagem de erro.
# else -> usado quando deu certo 
# finally -> usado tanto "certo/falha" mais visto como enceramento do programa
def somar(a,b):
    return(a+b)
a = int(input("Digite o primeiro número:\n"))
b = int(input("Digite o segundo número:\n  "))
resultado = somar(a,b)
#try usado em operacao onde pode dar erro.
try:
    a,b !=int
    print("O resultado é", resultado)
# except usado quando falhou
except Exception as erro:    
    print("Ocorreu um erro:",erro )
finally:
    print("Volte sempre :)")
print(somar(a,b))
