
while True:
    partidas = int(input())
    if partidas == 0:
        break
    
    jogador1 = jogador2 = 0
    for i in range(partidas):
        a, b = map(int, input().split())

        if a > b:
            jogador1 += 1
        elif a < b:
            jogador2 += 1

    print(jogador1, jogador2)
