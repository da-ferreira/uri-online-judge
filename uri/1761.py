
from math import tan, radians

while True:
    try:
        angulo, teodolito, arvore = map(float, input().split())

        resultado = (tan(radians(angulo)) * teodolito) + arvore
        resultado *= 5

        print(f'{resultado :.2f}')
    except EOFError:
        break
