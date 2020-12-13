
from math import sqrt

numero = int(input())
fib = ((((1 + sqrt(5)) / 2) ** numero) - (((1 - sqrt(5)) / 2) ** numero)) / sqrt(5)
print(round(fib, 1))
