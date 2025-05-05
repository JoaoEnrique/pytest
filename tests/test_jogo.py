from codigo.jogo import *

def test_quando_fun_pense_num_numero_recebe_qualquer_valor_retorna_3():
    valor = 5
    resposta = pense_num_numero(valor)
    assert resposta == 3