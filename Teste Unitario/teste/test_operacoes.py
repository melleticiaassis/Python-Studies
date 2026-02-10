import pytest
from src.calculadora.operacoes import soma


def test_soma_deve_somar_dois_numeros():
    # Arrange (organizar)
    a, b = 2, 3

    # Act (agir)
    resultado = soma(a, b)

    # Assert (verificar)
    assert resultado == 5


# Forma mais profissional, ao invés de escrever vários testes
@pytest.mark.parametrize(
    "a,b,esperado",
    [
        (2, 3, 5),      # Soma positivos
        (0, 0, 0),      # Soma zeros
        (-1, 1, 0),     # Soma negativo com positivo
        (1.5, 2.5, 4.0) # Soma floats
    ],
)
def test_soma_varios_casos(a, b, esperado):
    assert soma(a, b) == esperado
    