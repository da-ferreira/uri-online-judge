
from itertools import combinations_with_replacement
from math import factorial


def conta_permutacao(permutacao):
    temp = {
        1: permutacao.count(1),
        2: permutacao.count(2),
        3: permutacao.count(3),
        4: permutacao.count(4),
        5: permutacao.count(5),
        6: permutacao.count(6)
    }

    soma = 1

    for i in temp:
        if temp[i] > 1:
            soma *= factorial(temp[i])
    
    return factorial(len(permutacao)) // soma


casos = int(input())

for i in range(casos):
    palpite, dados = map(int, input().split())

    qtd = 0
    espaco_amostral = 6 ** dados
    combinacoes = list(combinations_with_replacement([1, 2, 3, 4, 5, 6], dados))

    for jogada in combinacoes:
        if sum(jogada) == palpite:
            qtd += conta_permutacao(jogada)
            
    print(f'{qtd / espaco_amostral :.15f}')
