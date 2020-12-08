
from operator import itemgetter

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    jogadores = {}

    for i in range(n):
        temp = input().split()

        for j in range(m):
            if temp[j] not in jogadores:
                jogadores[temp[j]] = 1
            else:
                jogadores[temp[j]] += 1

    jogadores = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
    jogadores.pop(0)

    maior = jogadores[0][1]

    segundo_lugar = []
    
    for a, b in jogadores:
        if b == maior:
            segundo_lugar.append(int(a))

    segundo_lugar.sort()

    for i in range(len(segundo_lugar)):
        print(segundo_lugar[i], end=' ')
    print()
