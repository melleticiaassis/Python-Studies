# # teste soma
# import pytest
# from src.calculadora.operacoes import soma

# def test_soma_deve_soamr_dois_numeros():
#     a,b = 2,3
#     resultado = soma(a,b)
#     assert resultado == 5
    
# @pytest.mark.parametrize(
#     "a,b,esperado",
#     [
#         (2, 3, 5),
#         (0, 0, 0),
#         (-1, 1, 0),
#         (1.5, 2.5, 4.0),
#     ],
# )

# def test_soma_valores_casos(a, b, esperado):
#     assert soma(a, b) == esperado
    
# #teste subtracao
# import pytest
# from src.calculadora.operacoes import subtracao

# def test_subtracao_deve_subtrair_valor():
#     a,b = 5,3
#     resultado = subtracao(a,b)
#     assert resultado
    
# @pytest.mark.parametrize(
#     "a,b,esperado",
#     [
#       (5, 3, 2),
#       (10, 6, 4),
#       (0, 0, 0), 
#       (3, 5, -2),
#     ],
# )
# def test_subtracao_valores_caso(a, b, esperado):
#     assert subtracao(a, b) == esperado
      
# # teste divisao    
# import pytest
# from src.calculadora.operacoes import divisao

# def test_divisao_deve_dividir_valor():
#     with pytest.raises(ZeroDivisionError):
#         divisao(10, 0)
        
#     a,b = 10,2
#     resultado = divisao(a,b)
#     return resultado

# @pytest.mark.parametrize(
#     "a,b,esperado",
#     [
#         (10, 2, 5),
#         (10, 0, 0),
#         (25, 5,  5),
#     ]
# )
# def test_divisao_valores_caso(a, b, esperado):
#     assert divisao(a, b) == esperado
    
  
    
import pytest
from src.calculadora.operacoes import soma, subtracao, divisao


def test_soma_deve_somar_dois_numeros():
    a, b = 2, 3
    resultado = soma(a, b)
    assert resultado == 5


@pytest.mark.parametrize(
    "a,b,esperado",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (1.5, 2.5, 4.0),
    ],
)
def test_soma_valores_casos(a, b, esperado):
    assert soma(a, b) == esperado


def test_subtracao_deve_subtrair_valor():
    a, b = 5, 3
    resultado = subtracao(a, b)
    assert resultado == 2


@pytest.mark.parametrize(
    "a,b,esperado",
    [
        (5, 3, 2),
        (10, 6, 4),
        (0, 0, 0),
        (3, 5, -2),
    ],
)
def test_subtracao_valores_caso(a, b, esperado):
    assert subtracao(a, b) == esperado


def test_divisao_deve_dividir_valor():
    with pytest.raises(ZeroDivisionError):
        divisao(10, 0)

    a, b = 10, 2
    resultado = divisao(a, b)
    assert resultado == 5


@pytest.mark.parametrize(
    "a,b,esperado",
    [
        (10, 2, 5),
        (25, 5, 5),
    ],
)
def test_divisao_valores_caso(a, b, esperado):
    assert divisao(a, b) == esperado