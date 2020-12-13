
def posicao_ventilador(linha, direita=True):

    if direita:
        for i in range(1, len(linha)):
            if linha[i] != '0':
                return int(linha[i])
    else:
        for i in range(len(linha) - 1,  -1, -1):
            if linha[i] != '0':
                return int(linha[i])


while True:
    linhas, colunas, posicao = map(int, input().split())
    if linhas == 0:
        break

    caixa = []

    for i in range(linhas):
        caixa.append(input().split())

    balao = [0, posicao - 1]  # linha, coluna
    estourado = False

    for i in range(linhas):
        vent_direita = posicao_ventilador(caixa[balao[0]][balao[1]:])
        vent_esquerda = posicao_ventilador(caixa[balao[0]][0:balao[1]], direita=False)

        if vent_direita > vent_esquerda:
            diferenca = vent_direita - vent_esquerda

            while diferenca > 0:
                balao[1] -= 1
                diferenca -= 1

                if caixa[balao[0]][balao[1]] != '0':
                    estourado = True
                    break
            
            if estourado:
                break
        
        elif vent_esquerda > vent_direita:
            diferenca = vent_esquerda - vent_direita

            while diferenca > 0:
                balao[1] += 1
                diferenca -= 1
            
                if caixa[balao[0]][balao[1]] != '0':
                    estourado = True
                    break
            
            if estourado:
                break
        
        balao[0] += 1

        if balao[0] == linhas:
            break

        elif caixa[balao[0]][balao[1]] != '0':
            estourado = True
            break

    if estourado:
        print(f'BOOM {balao[0] + 1} {balao[1] + 1}')
    else:
        print(f'OUT {balao[1] + 1}')
