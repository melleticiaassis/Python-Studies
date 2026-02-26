import pytest 
from src.usuario.usuario_valido import validar_usuario

def test_nome_vazio():
    with pytest.raises(ValueError):
        validar_usuario("",20)
        
def test_idade_negativa():
    with pytest.raises(ValueError):
        validar_usuario("", -1)

@pytest.mark.parametrize(
    "nome, idade, esperado",
    [
        ("Luca", 19, "maior"),
        ("Ana", 5, "menor"),
        ("João", 30, "maior"),
    ],
)

def test_validar_usuario(nome, idade, esperado):
    assert validar_usuario(nome, idade) == esperado 