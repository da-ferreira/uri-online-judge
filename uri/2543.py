
while True:
    try:
        gameplays, identificador = map(int, input().split())
        dados = []
        quantidade = 0
    
        for i in range(gameplays):
            dados.append(list(map(int, input().split())))

        for j in dados:
            if j[0] == identificador and j[1] == 0:
                quantidade += 1
        
        print(quantidade)
    except EOFError:
        break
