
from math import sqrt

while True:
    try:
        a, b, c = map(float, input().split())
        pi = 3.1415926535897

        semi_p = (a + b + c) / 2
        area_triangulo_temp = sqrt(semi_p * (semi_p - a) * (semi_p - b) * (semi_p - c))

        circulo_interno = pi * (area_triangulo_temp / semi_p) ** 2
        area_triangulo = area_triangulo_temp -  circulo_interno 

        raio_circulo_externo = (a * b * c) / (sqrt((a+b+c) * (b + c - a) *  (c + a - b) * (a + b - c)))
        circulo_externo = pi * raio_circulo_externo ** 2
        circulo_externo -= area_triangulo_temp

        print(f'{circulo_externo :.4f} {area_triangulo :.4f} {circulo_interno :.4f}')
    except EOFError:
        break
