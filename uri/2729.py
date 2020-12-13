
casos = int(input())

for i in range(casos):
    lista = set(input().split())
    lista = list(lista)
    lista.sort(key=str.casefold)

    print(' '.join(lista))
