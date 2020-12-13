
from operator import itemgetter

lista = []

qtd = int(input())

for i in range(qtd):
    entrada = input().split()
    
    temp = entrada[1:]
    temp = [int(x) for x in temp]

    temp.insert(0, entrada[0])

    lista.append(temp)

lista = sorted(lista, key=itemgetter(0))
lista = sorted(lista, key=itemgetter(3), reverse=True)
lista = sorted(lista, key=itemgetter(2), reverse=True)
lista = sorted(lista, key=itemgetter(1), reverse=True)

for a1, a2, a3, a4 in lista:
    print(a1, a2, a3, a4)
