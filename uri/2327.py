
n = int(input())
quadrado = []

for i in range(n):
    quadrado.append(list(map(int, input().split())))

somas = []
temp = 0

for i in range(n):  # linhas
    somas.append(sum(quadrado[i]))
    temp += quadrado[i][i]  # diagonal principal

somas.append(temp)

for i in range(n):  # colunas
    temp = 0

    for j in range(n):
        temp += quadrado[j][i]

    somas.append(temp)

temp = 0
j = n - 1
for i in range(n):  # diagonal secundária
    temp += quadrado[i][j]
    j -= 1

somas.append(temp)

if len(set(somas)) == 1:
    print(somas[0])
else:
    print(-1)
