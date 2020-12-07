from math import sqrt

p1 = input().split(' ')  # <- (x, y) do primeiro valor.
p2 = input().split(' ')  # <- (x, y) do segundo valor.

x1 = float(p1[0])
y1 = float(p1[1])

x2 = float(p2[0])
y2 = float(p2[1])

subtracao1 = x2 - x1
subtracao2 = y2 - y1

expo1 = subtracao1 ** 2
expo2  = subtracao2 ** 2

soma = expo1 + expo2
resultado = sqrt(soma)

print('{:.4f}'.format(resultado))
