import pytest
from src.validacao.idade_valida import validar_idade

@pytest.mark.parametrize(
    "idade, esperado",
    [
        (18, True),    # Exatamente 18 anos → maior de idade
        (19, True),    # Maior de idade
        (17, False),   # Menor de idade
        (0, False),    # Menor de idade
        (100, True),   # Idoso
    ],
)
def test_valida_maior_idade(idade, esperado):
    resultado = validar_idade(idade)
    assert resultado == esperado


def test_valida_idade_negativa():
    with pytest.raises(ValueError):
        validar_idade(-1)