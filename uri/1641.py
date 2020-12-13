
from math import sqrt

i = 1
while True:
    entrada = list(map(int, input().split()))
    if entrada[0] == 0:
        break

    raio = entrada.pop(0)
    largura = entrada.pop(0)
    altura = entrada.pop(0)

    diagonal = sqrt(abs(largura ** 2) + abs(altura ** 2))

    if diagonal <= raio * 2:
        print(f'Pizza {i} fits on the table.')
    else:
        print(f'Pizza {i} does not fit on the table.')

    i += 1
