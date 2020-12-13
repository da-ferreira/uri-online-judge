
while True:
    try:
        n, gols_comprar = map(int, input().split())
        
        pontos = 0
        partidas = []

        for i in range(n):
            meu_time, adversario = map(int, input().split())
            
            if meu_time > adversario:
                pontos += 3
                
            elif meu_time == adversario:
                partidas.insert(0, [meu_time, adversario, (adversario - meu_time)])
            else:
                partidas.append([meu_time, adversario, (adversario - meu_time)])

        partidas = sorted(partidas, key=lambda partidas: partidas[2])  # ordenando conforme a diferenca de pontos.
        
        for i in range(len(partidas)):
            if partidas[i][0] == partidas[i][1] and gols_comprar > 0:
                pontos += 3
                gols_comprar -= 1

            elif partidas[i][0] == partidas[i][1] and gols_comprar == 0:
                pontos += 1

            else:
                if (partidas[i][0] + gols_comprar) > partidas[i][1]:
                    gols_comprar -= ((partidas[i][1] - partidas[i][0]) + 1)
                    pontos += 3
                elif (partidas[i][0] + gols_comprar) == partidas[i][1]:
                    gols_comprar = 0
                    pontos += 1

        print(pontos)
    except EOFError:
        break
