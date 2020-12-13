
jogadores, rodadas = map(int, input().split())

pontos_jogadores = list(map(int, input().split()))

maior = [0, 1]

for i in range(jogadores):
    soma = sum(pontos_jogadores[i::jogadores])

    if soma >= maior[0]:
        maior[0] = soma
        maior[1] = i + 1

print(maior[1])
