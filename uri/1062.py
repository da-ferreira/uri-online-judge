
while True:
    blocos = int(input())
    if blocos == 0:
        break

    while True:
        trens = list(map(int, input().split()))
        if trens[0] == 0:
            break

        tiragem = blocos
        estacao = []
        eh_possivel = True

        while True:
            if len(trens) > 0 and trens[-1] == tiragem:
                trens.pop()
                tiragem -= 1
            else:
                if len(trens) == 0 and len(estacao) > 0 and estacao[-1] != tiragem:
                    eh_possivel = False
                    break
                
                if len(estacao) > 0 and estacao[-1] == tiragem:
                    tiragem -= 1
                    estacao.pop()
                
                else:
                    if len(trens) > 0:
                        estacao.append(trens.pop())

                    if tiragem == 0:
                        break

        if eh_possivel:
            print('Yes')
        else:
            print('No')
    
    print()
