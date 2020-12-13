
quantidade = int(input())

for i in range(quantidade):
    texto = input()
    palavra = input()
    
    posicoes = []
    temp = ''

    for j in range(len(texto)):
        if texto[j] != ' ':
            temp += texto[j]     
        else:
            if temp == palavra:
                posicoes.append(str(j - len(palavra)))
            
            temp = ''
    
    if temp == palavra:
        posicoes.append(str(j - (len(palavra) - 1)))

    if len(posicoes) > 0:
        print(' '.join(posicoes))
    else:
        print(-1)
