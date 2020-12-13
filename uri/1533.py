
while True:
    quantidade = int(input())
    if quantidade == 0:
        break

    suspeitos = list(map(int, input().split()))

    indice_maior = suspeitos.index(max(suspeitos))
    suspeitos[indice_maior] = 0

    assassino = suspeitos.index(max(suspeitos)) + 1
    print(assassino)
