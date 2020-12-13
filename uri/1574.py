
casos = int(input())

for i in range(casos):
    n = int(input())
    instrucoes = []

    posicao = 0

    for j in range(n):
        instrucao = input().split()

        if len(instrucao) == 1 and instrucao[0] == 'LEFT':
            posicao -= 1
            instrucoes.append('LEFT')
        elif len(instrucao) == 1 and instrucao[0] == 'RIGHT':
            posicao += 1
            instrucoes.append('RIGHT')
        
        else:
            if instrucoes[int(instrucao[2]) - 1] == 'LEFT':
                posicao -= 1
                instrucoes.append('LEFT')
            elif instrucoes[int(instrucao[2]) - 1] == 'RIGHT':
                posicao += 1
                instrucoes.append('RIGHT')
    
    print(posicao)
