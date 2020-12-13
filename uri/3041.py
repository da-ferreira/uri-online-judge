
while True:
    quantidade = int(input())
    if quantidade == 0:
        break

    revisores = []
    soma = 0

    for i in range(quantidade):
        entrada = int(input())
        revisores.append([entrada, 0])
        soma += entrada
    
    revisores.sort(key=lambda k: k[0], reverse=True)
    artigos = int(input())

    if artigos > soma:
        print('Impossible')
    else: 
        i = 0

        while artigos > 0:
            if revisores[i][1] < revisores[i][0]:
                revisores[i][1] += 1
                artigos -= 1

            if i >= len(revisores) - 1:
                i = 0
            else:
                i += 1

        for x in revisores:
            print(x[1])
