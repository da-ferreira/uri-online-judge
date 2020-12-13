
from math import factorial

numero = int(input())
soma = quantidade = 0


while soma != numero:
    temp = 0
    i = 1
    while True:
        temp = factorial(i)
        if (temp + soma) > numero:
            soma += factorial(i-1)
            quantidade += 1
            break
        i += 1

print(quantidade)
