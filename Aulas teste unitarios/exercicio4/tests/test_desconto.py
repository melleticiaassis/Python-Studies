import pytest
from src.calcular.desconto import calcular_desconto

@pytest.mark.parametrize(
    "preco, porcentagem, esperado",
    [
        (100.00, 0,    100.00),
        (200.00, 10,   180.00),
        (150.50, 100,  0.00),
        (99.99,  15,   84.99),
        (250.00, 7,    232.50),
        (77.77,  0,    77.77),
        (500.00, 100,  0.00),
        (0.00,   30,   0.00),
    ],
)
def test_aplicar_desconto(preco, porcentagem, esperado):  
    # Testa diferentes cenários válidos de aplicação de desconto.
    assert calcular_desconto(preco, porcentagem) == esperado

# Testes de erro (validação de exceções)
def test_preco_negativo():
    #Deve gerar erro quando o preço for negativo.   
    with pytest.raises(ValueError, match="preço não pode ser negativo"):
        calcular_desconto(-10, 10)

def test_porcentagem_negativa():
    #Deve gerar erro quando a porcentagem for menor que 0.  
    with pytest.raises(ValueError):
        calcular_desconto(100, -5)

def test_porcentagem_maior_que_100():   
    #Deve gerar erro quando a porcentagem for maior que 100.
    with pytest.raises(ValueError):
        calcular_desconto(100, 150)