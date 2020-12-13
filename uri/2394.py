
n, m = map(int, input().split())

competidores = []

for i in range(1, n + 1):
    voltas = list(map(int, input().split()))

    competidores.append([i, sum(voltas)])

competidores.sort(key=lambda k: k[1])

print(competidores[0][0])
