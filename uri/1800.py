
qtd_escritorios, qdt_escritorios_dias = map(int, input().split())

escritorios_vistos = list(map(int, input().split()))

for i in range(qtd_escritorios):
    numero = int(input())
    
    if numero in escritorios_vistos:
        print(0)
    else:
        print(1)
        escritorios_vistos.append(numero)
