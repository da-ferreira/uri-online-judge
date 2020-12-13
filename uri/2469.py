
qtd_notas = int(input())

notas = list(map(int, input().split()))

frequencia = {}

for i in range(qtd_notas):
    if notas[i] not in frequencia:
        frequencia[notas[i]] = 1
    else:
        frequencia[notas[i]] += 1

temp = []

for i in frequencia:
    if frequencia[i] == max(frequencia.values()):
        temp.append(i)

print(max(temp))
