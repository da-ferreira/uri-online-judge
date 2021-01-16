
while True:
    quantidade = int(input())
    if quantidade == 0:
        break

    carros = []

    for i in range(quantidade):
        numero, temp = map(int, input().split())
        carros.append([numero, temp, i])
    
    ranking = [0] * quantidade
    INVALIDO = False

    for i in range(quantidade):
        if carros[i][2] + carros[i][1] < 0 or carros[i][2] + carros[i][1] > quantidade - 1:
            INVALIDO = True
            break
        else:
            if ranking[carros[i][2] + carros[i][1]] != 0:
                INVALIDO = True
                break
            
            ranking[carros[i][2] + carros[i][1]] = carros[i][0]
    
    if INVALIDO:
        print(-1)
    else:
        print(' '.join(str(x) for x in ranking))


    