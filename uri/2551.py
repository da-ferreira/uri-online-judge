
while True:
    try:
        treinos = int(input())

        for i in range(treinos):
            duracao, distancia = map(int, input().split())

            if i == 0:
                print(i+1)
                media = distancia / duracao
            elif (distancia / duracao) > media:
                print(i+1)
                media = distancia / duracao
    except EOFError:
        break
