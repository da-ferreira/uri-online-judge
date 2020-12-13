
# L, R, U e D (L-Esquerda, R-Direita, U-Cima, D-Baixo)

while True:
    linhas, colunas, qtd_i = map(int, input().split())
    if linhas == 0:
        break

    mapa = []
    pacman = [0, 0]  # x e y do pacman (coordenadas)
    direcao = 'direita'

    for i in range(linhas):
        mapa.append(list(input()))

        if '<' in mapa[-1]:
            pacman[0] = i
            pacman[1] = mapa[-1].index('<')
    
    instrucoes = input()
    pastilhas = 0
    
    for i in range(qtd_i):
        if instrucoes[i] != 'W':
            if instrucoes[i] == 'L':
                direcao = 'esquerda'
            
            elif instrucoes[i] == 'R':
                direcao = 'direita'
            
            elif instrucoes[i] == 'U':
                direcao = 'cima'
            
            if instrucoes[i] == 'D':
                direcao = 'baixo'
        else:
            if direcao == 'cima' and mapa[pacman[0] - 1][pacman[1]] != '#':
                if mapa[pacman[0] - 1][pacman[1]] == '*':
                    pastilhas += 1  ##
                    mapa[pacman[0] - 1][pacman[1]] = ' '
                
                pacman[0] -= 1
            
            elif direcao == 'baixo' and mapa[pacman[0] + 1][pacman[1]] != '#':
                if mapa[pacman[0] + 1][pacman[1]] == '*':
                    pastilhas += 1  ##
                    mapa[pacman[0] + 1][pacman[1]] = ' '
                
                pacman[0] += 1
            
            elif direcao == 'direita' and mapa[pacman[0]][pacman[1] + 1] != '#':
                if mapa[pacman[0]][pacman[1] + 1] == '*':
                    pastilhas += 1  ##
                    mapa[pacman[0]][pacman[1] + 1] = ' '
                
                pacman[1] += 1

            elif direcao == 'esquerda' and mapa[pacman[0]][pacman[1] - 1] != '#':
                if mapa[pacman[0]][pacman[1] - 1] == '*':
                    pastilhas += 1  ##
                    mapa[pacman[0]][pacman[1] - 1] = ' '
                
                pacman[1] -= 1
    
    print(pastilhas)
