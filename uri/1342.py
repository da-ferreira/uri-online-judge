
while True:
    qtd_jogadores, trilha = map(int, input().split())
    if qtd_jogadores == 0 and trilha == 0:
        break

    armadilhas = set(map(int, input().split()))

    jogadores = {
        x: [0, False] for x in range(1, qtd_jogadores + 1)
    }

    qtd_jogos = int(input())
    rodada = 1
    vencedor = ''

    for i in range(qtd_jogos):
        dados = sum(list(map(int, input().split())))

        if vencedor == '':
            while jogadores[rodada][1]:
                jogadores[rodada][1] = False
                
                if rodada == qtd_jogadores:
                    rodada = 1
                else:
                    rodada += 1
            
            jogadores[rodada][0] += dados

            if jogadores[rodada][0] in armadilhas:
                jogadores[rodada][1] = True  # caiu numa armadilha

            if jogadores[rodada][0] > trilha:
                vencedor = rodada

            if rodada == qtd_jogadores:
                rodada = 1
            else:
                rodada += 1
            
    print(vencedor)
