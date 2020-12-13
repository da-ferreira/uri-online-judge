
while True:
    try:
        linhas, colunas = map(int, input().split())
        mapa = []
        zeros = 0

        for i in range(linhas):
            mapa.append(input().split())
            zeros += mapa[-1].count('0')

            if i == 0:
                x = 0
                y = mapa[-1].index('X')

        instrucoes = ''

        for i in range(zeros):
            if i == 0:
                if mapa[x + 1][y] == '0':
                    x += 1
                    instrucoes += 'F '
                    direcao = 'sul'
                
                elif y > 0 and mapa[x][y - 1] == '0':
                    y -= 1
                    instrucoes += 'R '
                    instrucoes += 'F '
                    direcao = 'oeste'
                
                elif y < colunas - 1 and mapa[x][y + 1] == '0':
                    y += 1
                    instrucoes += 'L '
                    instrucoes += 'F '
                    direcao = 'leste'
            else:
                if x < linhas - 1 and mapa[x + 1][y] == '0' and direcao != 'norte':
                    if direcao == 'sul':
                        instrucoes += 'F '

                    elif direcao == 'oeste':
                        instrucoes += 'L '
                        instrucoes += 'F '
                        
                    elif direcao == 'leste':
                        instrucoes += 'R '
                        instrucoes += 'F '

                    x += 1
                    direcao = 'sul'

                elif x > 0 and mapa[x - 1][y] == '0' and direcao != 'sul':
                    if direcao == 'norte':
                        instrucoes += 'F '

                    elif direcao == 'oeste':
                        instrucoes += 'R '
                        instrucoes += 'F '

                    elif direcao == 'leste':
                        instrucoes += 'L '
                        instrucoes += 'F '

                    x -= 1
                    direcao = 'norte'
                    
                elif y < colunas - 1 and mapa[x][y + 1] == '0' and direcao != 'oeste':
                    if direcao == 'leste':
                        instrucoes += 'F '

                    elif direcao == 'norte':
                        instrucoes += 'R '
                        instrucoes += 'F '

                    elif direcao == 'sul':
                        instrucoes += 'L '
                        instrucoes += 'F '
                    
                    y += 1
                    direcao = 'leste'

                elif y > 0 and mapa[x][y - 1] == '0' and direcao != 'leste':
                    if direcao == 'oeste':
                        instrucoes += 'F '
                    
                    elif direcao == 'norte':
                        instrucoes += 'L '
                        instrucoes += 'F '

                    elif direcao == 'sul':
                        instrucoes += 'R '
                        instrucoes += 'F '

                    y -= 1
                    direcao = 'oeste' 

        print(instrucoes + 'E ')
    except EOFError:
        break
