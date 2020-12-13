
from math import tan, radians

casos = int(input())

for i in range(casos):
    lado = int(input())

    lado /= 2
    altura_triangulo = lado / tan(radians(36))
    area_triangulo = 1/2 * lado * altura_triangulo

    area_pentagono = area_triangulo * 10

    print(f'{area_pentagono :.3f}')
