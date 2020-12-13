
quantidade = int(input())
caixas = list(map(int, input().split()))
caixas.sort()

teste = 0

if caixas[0] > 8:
    teste = -1
else:
    for i in range(quantidade - 1):
        if abs(caixas[i] - caixas[i + 1]) <= 8:
            teste += 1

if teste == quantidade - 1:
    print('S')
else:
    print('N')
