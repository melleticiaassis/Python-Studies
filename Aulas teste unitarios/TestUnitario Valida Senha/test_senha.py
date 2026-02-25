import pytest
from senha import senha_valida

@pytest.mark.parametrize("senha, esperado", [
    ("abc12345", True),
    ("abc123", False),
    ("abcdefghi", False),
    ("12345678", True),
])

def test_senha_valida_(senha, esperado):
    assert senha_valida(senha) == esperado

#pytest.raises -> forma de testar uma funcao se lancar erro.abs

def test_tipo_invalido():
    with pytest.raises(TypeError):
        senha_valida(123)
