
from math import sqrt

while True:
    try:
        r1, x1, y1, r2, x2, y2 = map(int, input().split())
        
        distancia_entre_centros = sqrt(abs((x2 - x1) ** 2) + abs((y2 - y1) ** 2))
        
        if r1 >= (distancia_entre_centros + r2):
            print('RICO')
        else:
            print('MORTO')
    except:
        break