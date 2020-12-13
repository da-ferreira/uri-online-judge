
n_carros, n_voltas = map(int, input().split())

tempo = []

for i in range(1, n_carros + 1):
    voltas = list(map(int, input().split()))

    tempo.append([i, sum(voltas)])

tempo.sort(key=lambda k: k[1])

for i in range(3):
    print(tempo[i][0])
