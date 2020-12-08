
from math import sqrt, floor

casos = int(input())

for i in range(casos):
    numero = int(input())
    piso_sqrt = floor(sqrt(numero))

    divisores = 0

    for j in range(1, piso_sqrt+1):
        if numero % j == 0:
            divisores += 1
    
    if divisores == 1:
        print('Prime')
    else:
        print('Not Prime')
