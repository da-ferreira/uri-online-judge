
fila_incial_qtd = int(input())
inicial = list(map(int, input().split()))

fila_sairam = int(input())
sairam = list(map(int, input().split()))

for identificador in sairam:
    inicial.remove(identificador)

for i in range(len(inicial)):
    if i != (len(inicial) - 1):
        print(inicial[i], end=' ')
    else:
        print(inicial[i])
