import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import codigo.calculadora as c

# indicado escrever nome das funcoes detalhadas
def test_quando_soma_receber_4_e_3_retorna_7():
    # assert True
    entrada1 = 4
    entrada2 = 3
    esperado = 7
    resultado = c.soma(entrada1, entrada2)
    assert resultado == esperado, f"Esperado {esperado}, mas obteve {resultado}"
    
