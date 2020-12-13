
quantidade = int(input())
montes = []

for i in range(quantidade):
    distancia, tonalidade = map(int, input().split())
    montes.append([distancia, tonalidade])

montes.sort(key=lambda k: k[0])
verdade = True

for i in range(1, quantidade):
    if montes[i][1] > montes[i - 1][1]:
        verdade = False
        break

if verdade:
    print('S')
else:
    print('N')
