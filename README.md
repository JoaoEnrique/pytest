## Metodologia GWT e AAA
Exemplo:
```py
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
    
```

# Flags
Flags utilizadas para o pytest

### Mostrar mais detalhes do erro
```bash
pytest -v
```

### Interromper todos os testes se falhar
```bash
pytest -x
```

### Modo debug
```bash
pytest --pdb
```

### Rodar testes especificos
```bash
# roda todos os testes com palavra soma no nome da função
pytest -k "soma"
```

## test/test_calculadora.py
```py
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
```


## test/jogo.py
```py
from codigo.jogo import *

def test_quando_fun_pense_num_numero_recebe_qualquer_valor_retorna_3():
    valor = 5
    resposta = pense_num_numero(valor)
    assert resposta == 3
```


```py
# esse testa vai passar
def test_deve_falhar():
    assert (1,2,3) == (1,2,4)
```

## Rodar testes
```bash
#rodar todos os testes
pytest

#rodar teste especifico pytest testes/test_one.py

```

## Resultado
```bash
C:\Users\joao\projetos\pytest>pytest
=============================================================================== test session starts ================================================================================
platform win32 -- Python 3.13.2, pytest-8.3.5, pluggy-1.5.0
rootdir: C:\Users\joao\projetos\pytest
collected 3 items                                                                                                                                                                   

tests\test_calculadora.py ..                                                                                                                                                  [ 66%] 
tests\test_jogo.py .                                                                                                                                                          [100%] 

================================================================================ 3 passed in 0.03s =================================================================================
```