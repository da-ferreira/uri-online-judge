
def quantidade_palavras(caca_palavra, palavra, linha, coluna):

    quantidade = 0

    if len(palavra) == 1:
        for i in range(linha):
            quantidade += caca_palavra[i].count(palavra)
    else:        
        for i in range(linha):  # horizontal
            temp = ''

            j = k = 0
            while j < coluna:
                temp += caca_palavra[i][j]

                if len(temp) == len(palavra):
                    if temp == palavra:
                        quantidade += 1
                    temp = ''
                    k += 1
                    j = k
                else:
                    j += 1
            
            if temp == palavra:
                quantidade += 1

        for i in range(coluna):  # vertical
            temp = ''

            j = k = 0
            while j < linha:
                temp += caca_palavra[j][i]

                if len(temp) == len(palavra):
                    if temp == palavra:
                        quantidade += 1
                    temp = ''
                    k += 1
                    j = k
                
                else:
                    j += 1

    return quantidade


casos = int(input())

for i in range(casos):
    l, c = map(int, input().split())
    hunting_words = []

    for j in range(l):
        hunting_words.append(input())
    
    qtd_palavras = int(input())

    for j in range(qtd_palavras):
        palavra = input()

        print(quantidade_palavras(hunting_words, palavra, l, c))
