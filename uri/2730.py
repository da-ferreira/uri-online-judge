
from math import gcd

while True:
    quantidade = int(input())
    if quantidade == 0:
        break

    conjunto_a = list(map(int, input().split()))
    conjunto_b = list(map(int, input().split()))

    pares = set()

    resultado = 0

    for i in range(quantidade):
        for j in range(quantidade):
            if gcd(conjunto_a[i], conjunto_b[j]) == 1 and f'{conjunto_a[i]} {conjunto_b[j]}' not in pares:
                resultado += 1
                pares.add(f'{conjunto_a[i]} {conjunto_b[j]}')

    for i in range(quantidade):
        for j in range(quantidade):
            if gcd(conjunto_b[i], conjunto_a[j]) == 1 and f'{conjunto_b[i]} {conjunto_a[j]}' not in pares:
                resultado += 1
                pares.add(f'{conjunto_b[i]} {conjunto_a[j]}')

    print(resultado)

