
while True:
    linhas, colunas, qtd_fila = map(int, input().split())
    if linhas == 0 and colunas == 0 and qtd_fila == 0:
        break

    blocos = []

    for i in range(linhas):
        blocos.append(input().split())

    fila = input().split()

    for i in range(qtd_fila):
        j = colunas - 1

        while j > -1:
            if blocos[0][j] == '0':
                
                k = 0
                while k + 1 < linhas and blocos[k + 1][j] == '0':
                    k += 1

                blocos[k][j] = fila.pop(0)
                break

            j -= 1    

    for i in range(linhas):
        print(' '.join(blocos[i]))
    