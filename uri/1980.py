
from math import factorial

while True:
    caracteres = input().strip()
    if len(caracteres) == 1 and caracteres == '0':
        break

    print(factorial(len(caracteres)))
