import pytest
from scr.dobro import dobro

@pytest.mark.parametrize("numero, esperado", [
    (1, 2),
    (2, 4),
    (5, 10),
    (0, 0),
    (-1, -2),
])
def test_multiplicacao(numero, esperado):
    assert dobro(numero) == esperado


