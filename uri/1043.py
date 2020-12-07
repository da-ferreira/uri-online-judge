
valores = input().split(' ')

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

if ((b - c) < a < (b + c)) and \
        ((a - c) < b < (a + c)) and \
        ((a - b) < c < (a + b)):
    print('Perimetro = {:.1f}'.format(a + b + c))
else:
    trapezio = ((a + b) * c) / 2
    print('Area = {:.1f}'.format(trapezio))
