
valores = input().split()
for i in range(3):
    valores[i] = float(valores[i])

valores.sort(reverse=True)

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

if a >= (b + c):
    print('NAO FORMA TRIANGULO')
else:
    if pow(a, 2) == (pow(b, 2) + pow(c, 2)):
        print('TRIANGULO RETANGULO')
    if pow(a, 2) > (pow(b, 2) + pow(c, 2)):
        print('TRIANGULO OBTUSANGULO')
    if pow(a, 2) < (pow(b, 2) + pow(c, 2)):
        print('TRIANGULO ACUTANGULO')
    if (a == b) and (b == c) and (a == c):
        print('TRIANGULO EQUILATERO')
    if ((a == b) and (a != c)) or ((b == a) and (b != c)) or ((c == a) and (c != b))\
            or ((b == c) and (b != a)):
        print('TRIANGULO ISOSCELES')
