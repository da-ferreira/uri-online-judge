
n, m = map(int, input().split())

relatorio = [[], []]

for i in range(n):
    entrada = input().split()

    for i in range(m):
        if entrada[i][1] == 'V':
            relatorio[0].append(entrada[i])
        else:
            relatorio[1].append(entrada[i])

relatorio[0].sort(key=lambda k: k[0], reverse=True)
relatorio[1].sort(key=lambda k: k[0], reverse=True)

relatorio = relatorio[0] + relatorio[1]

for i in relatorio:
    print(i)
