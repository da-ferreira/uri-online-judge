
while True:
    try:
        integrantes = int(input())
        coral = list(map(int, input().split()))
        soma = sum(coral)

        if soma % integrantes != 0:
            print(-1)
        else:
            media = soma // integrantes
            compassos = 1

            for pessoa in coral:
                if pessoa < media:
                    compassos += media - pessoa
            
            print(compassos)
    except EOFError:
        break
