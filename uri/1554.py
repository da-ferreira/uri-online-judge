
from math import sqrt

casos = int(input())

for i in range(casos):
    qtd_bolas = int(input())

    branca_x, branca_y = map(int, input().split())
    bola_mais_perto = [float('inf'), 1]

    for j in range(qtd_bolas):
        bola_x, bola_y = map(int, input().split())
        distancia = sqrt(((bola_x - branca_x) ** 2) + ((bola_y - branca_y) ** 2))

        if distancia < bola_mais_perto[0]:
            bola_mais_perto[0] = distancia
            bola_mais_perto[1] = j + 1
    
    print(bola_mais_perto[1])
