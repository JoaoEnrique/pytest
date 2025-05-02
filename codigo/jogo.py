from codigo.calculadora import divisao, multiplicacao, soma, subtracao


def pense_num_numero(numero):
    passo_0 = numero + 5
    passo_1 = passo_0 * 2
    passo_2 = passo_1 - 4
    passo_3 = passo_2 / 2
    passo_4 = passo_3 - numero
    return passo_4 #sempre será = 4

def pense_num_numero2(numero):
    return subtracao(divisao(subtracao(multiplicacao(soma(numero, 5), 2), 4), 2), numero) # mesmo resultado