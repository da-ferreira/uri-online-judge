from math import sqrt, pow
valores = input().split(' ')

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

delta = pow(b, 2) - 4 * a * c

if a == 0 or delta < 0:
    print('Impossivel calcular')
else:
    x1_positivo = (-b + sqrt(delta)) / (2 * a)
    x2_negativo = (-b - sqrt(delta)) / (2 * a)

    print('R1 = {:.5f}'.format(x1_positivo))
    print('R2 = {:.5f}'.format(x2_negativo))
