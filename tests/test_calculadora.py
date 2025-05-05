import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import codigo.calculadora as c

"""
Metodologia GWT:
Give    -   Dado
When    -   Quando
Then    -   Então

Triplo A (AAA):
Arrange -   Dado
Act     -   Quando
Assert  -   Assert
"""

# indicado escrever nome das funcoes detalhadas
def test_quando_soma_receber_4_e_3_retorna_7():
    entrada1 = 4 # Given
    entrada2 = 3 # Given
    resultado = c.soma(entrada1, entrada2) # When
    esperado = 7 # Then
    assert resultado == esperado # Then
    
# TDD - Kent Beck - One-step Test
def test_quando_subtracao_recebe_2_e_1_entao_retorna_1():
    assert c.subtracao(2, 1) == 1