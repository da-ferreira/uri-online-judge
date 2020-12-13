
texto = input()

qtd_palavras = int(input())
palavras = input().split()

for i in range(qtd_palavras):
    temp = ''
    posicoes = []

    for j in range(len(texto)):
        if texto[j] != ' ':
            temp += texto[j]     
        else:
            if temp == palavras[i]:
                posicoes.append(str(j - len(palavras[i])))
            
            temp = ''
    if len(posicoes) > 0:
        print(' '.join(posicoes))
    else:
        print(-1)
