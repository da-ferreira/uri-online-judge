
from math import sqrt

def euclidian_distance(x2, y2):

    distancia = (abs(x2) ** 2) + (abs(y2) ** 2)
    distancia = sqrt(distancia)

    return distancia


def busca_binaria(vetor, item):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:  # Caso o item nao esteja na lista
        meio = (inicio + fim) // 2

        if (item <= vetor[meio] and meio == len(vetor) - 1) or \
             item <= vetor[meio] and meio < len(vetor) - 1 and vetor[meio + 1] < item:

            return meio

        elif item > vetor[meio]:
            fim = meio - 1
        
        elif item < vetor [meio]:
            inicio = meio + 1


circulos, tiros = map(int, input().split())

raios = []
pontos = 0

for i in range(circulos):
    raios.append(int(input()))

raios.reverse()

for i in range(tiros):
    x, y = map(int, input().split())

    distancia = euclidian_distance(x, y)

    if distancia <= raios[0]:
        point = busca_binaria(raios, distancia)

        pontos += (point + 1) 

print(pontos)
