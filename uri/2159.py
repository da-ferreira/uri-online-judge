
from math import log

numero = int(input())

p = numero / log(numero)
m = 1.25506 * (numero / log(numero))

print(f'{p :.1f} {m :.1f}')
