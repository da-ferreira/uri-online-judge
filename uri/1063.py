
while True:
    n = int(input())
    if n == 0:
        break

    vagoes = input().split()
    saida_desejada = input().split()
    
    estacao = []
    sequencia = ''

    i = 0
    while True:
        if i == 0:
            estacao.append(vagoes.pop(0))
            sequencia += 'I'
        else:
            if len(estacao) > 0 and estacao[-1] == saida_desejada[0]:
                saida_desejada.pop(0)
                estacao.pop()
                sequencia += 'R'
            
            else:
                if len(vagoes) == 0 and len(estacao) > 0 and estacao[-1] != saida_desejada[0]:
                    sequencia += ' Impossible'
                    break
                
                else:
                    if len(vagoes) == 0 and len(estacao) == 0:
                        break

                    estacao.append(vagoes.pop(0))
                    sequencia += 'I'

        i += 1

    print(sequencia)
