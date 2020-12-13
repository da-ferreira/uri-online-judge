
from math import sqrt

def euclidian_distance(x1, y1, x2, y2):
    from math import sqrt

    distancia = (abs(x2 - x1) ** 2) + (abs(y2 - y1) ** 2)
    distancia = sqrt(distancia)

    return distancia


while True:
    quantidade = int(input())
    if quantidade == 0:
        break

    cx, cy, raio_menor, raio_maior = map(int, input().split())
    
    pontos = [
        [0, 0],  # Chiquinha
        [0, 0]   # Popis
    ]

    for i in range(quantidade):
        x, y = map(int, input().split())  # chiquinha

        distancia = euclidian_distance(cx, cy, x, y)

        if distancia < raio_menor:
            pontos[0][0] += 1
        
        elif distancia >= raio_menor and distancia <= raio_maior:
            pontos[0][1] += 1
        
        x, y = map(int, input().split())  # popis

        distancia = euclidian_distance(cx, cy, x, y)

        if distancia < raio_menor:
            pontos[1][0] += 1
        
        elif distancia >= raio_menor and distancia <= raio_maior:
            pontos[1][1] += 1

    if pontos[0][0] > pontos[1][0]:
        print('C > P')
    
    elif pontos[1][0] > pontos[0][0]:
        print('P > C')
    else:
        if pontos[0][1] > pontos[1][1]:
            print('C > P')
    
        elif pontos[1][1] > pontos[0][1]:
            print('P > C')
        else:
            print('C = P')
