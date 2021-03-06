
quantidade = int(input())
criancas = list(map(int, input().split()))

criancas.sort()
presentes = 0

j = 1

for i in range(quantidade):
    if i == 0:
        presentes += j
    else:
        if criancas[i] > criancas[i - 1]:
            j += 1
            presentes += j
        else:
            presentes += j

print(presentes)
            