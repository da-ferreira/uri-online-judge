
while True:
    linhas, colunas, instrucoes = map(int, input().split())
    if linhas == 0 and colunas == 0 and instrucoes == 0:
        break
    
    matriz = []

    for i in range(linhas):
        temp = list(input())
        matriz.append(temp)

        if 'N' in temp:
            inicio = [i, temp.index('N'), 'N']
        elif 'S' in temp:
            inicio = [i, matriz[i].index('S'), 'S']
        elif 'L' in temp:
            inicio = [i, matriz[i].index('L'), 'L']
        elif 'O' in temp:
            inicio = [i, matriz[i].index('O'), 'O']  # i = linha, matriz[i] = coluna
    
    instruct = input()
    figurinhas = 0

    for i in range(instrucoes):
        if instruct[i] in 'DE':
            if (instruct[i] == 'E' and inicio[2] == 'N') or (instruct[i] == 'D' and inicio[2] == 'S'):
                inicio[2] = 'O'

            elif (instruct[i] == 'D' and inicio[2] == 'N') or (instruct[i] == 'E' and inicio[2] == 'S'):
                inicio[2] = 'L'
            
            elif (instruct[i] == 'E' and inicio[2] == 'O') or (instruct[i] == 'D' and inicio[2] == 'L'): 
                inicio[2] = 'S'
            
            elif (instruct[i] == 'D' and inicio[2] == 'O') or (instruct[i] == 'E' and inicio[2] == 'L'): 
                inicio[2] = 'N'

        
        if instruct[i] == 'F':
            if (inicio[2] == 'N') and (inicio[0] != 0) and (matriz[inicio[0] - 1][inicio[1]] != '#'):
                if matriz[inicio[0] - 1][inicio[1]] == '*':
                    figurinhas += 1
                    matriz[inicio[0] - 1][inicio[1]] = '.'
                    
                inicio[0] -= 1 

            elif (inicio[2] == 'S') and (inicio[0] != (linhas - 1)) and (matriz[inicio[0] + 1][inicio[1]] != '#'):        
                if matriz[inicio[0] + 1][inicio[1]] == '*':
                    figurinhas += 1
                    matriz[inicio[0] + 1][inicio[1]] = '.'
                
                inicio[0] += 1
            
            elif (inicio[2] == 'L') and (inicio[1] != (colunas - 1)) and (matriz[inicio[0]][inicio[1] + 1] != '#'):
                if matriz[inicio[0]][inicio[1] + 1] == '*':
                    figurinhas += 1
                    matriz[inicio[0]][inicio[1] + 1] = '.'
                
                inicio[1] += 1
            
            elif (inicio[2] == 'O') and (inicio[1] != 0) and (matriz[inicio[0]][inicio[1] - 1] != '#'):
                if matriz[inicio[0]][inicio[1] - 1] == '*':
                    figurinhas += 1
                    matriz[inicio[0]][inicio[1] - 1] = '.'
                
                inicio[1] -= 1
        
    print(figurinhas)
