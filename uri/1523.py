
while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break

    eh_possivel = True
    estacionamento = []

    for i in range(n):
        chegada, saida = map(int, input().split())

        if eh_possivel:
            if i == 0:
                estacionamento.append([chegada, saida])
            else:
                while len(estacionamento) > 0 and chegada >= estacionamento[-1][1]:
                    estacionamento.pop()
                
                if len(estacionamento) == 0:
                    estacionamento.append([chegada, saida])
                
                elif chegada <= estacionamento[-1][1] and saida > estacionamento[-1][1]:
                    eh_possivel = False
                
                elif chegada < estacionamento[-1][1] and saida < estacionamento[-1][1]:
                    while len(estacionamento) > 0 and chegada >= estacionamento[-1][1]:
                        estacionamento.pop()
                    
                    if len(estacionamento) < k:
                        estacionamento.append([chegada, saida])
                    else:
                        eh_possivel = False
        
    if eh_possivel:
        print('Sim')
    else:
        print('Nao')
