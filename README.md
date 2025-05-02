Os testes devem começar com "test_" para serem enxergados pelo pytest

```py
# esse testa vai passar
def test_deve_passar():
    assert (1,2,3) == (1,2,3)
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
(venv) joao@macbookpro aula1 % pytest
========================================== test session starts ==========================================
platform darwin -- Python 3.13.1, pytest-8.3.5, pluggy-1.5.0
rootdir: /Users/joao/Documents/PersonalProjects/python/aula1
collected 2 items                                                                                       

tests/test_one.py .                                                                               [ 50%]
tests/test_two.py F                                                                               [100%]

=============================================== FAILURES ================================================
___________________________________________ test_deve_falhar ____________________________________________

    def test_deve_falhar():
>       assert (1,2,3) == (1,2,4)
E       assert (1, 2, 3) == (1, 2, 4)
E         
E         At index 2 diff: 3 != 4
E         Use -v to get more diff

tests/test_two.py:3: AssertionError
======================================== short test summary info ========================================
FAILED tests/test_two.py::test_deve_falhar - assert (1, 2, 3) == (1, 2, 4)
====================================== 1 failed, 1 passed in 0.01s ======================================
(venv) joao@macbookpro aula1 % 
```