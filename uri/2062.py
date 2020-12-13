
qtd_palavras = int(input())
palavras = input().split()

for i in range(qtd_palavras):
    if palavras[i][0:2] == 'UR' and len(palavras[i]) == 3:
        palavras[i] = 'URI'
    elif palavras[i][0:2] == 'OB' and len(palavras[i]) == 3:
        palavras[i] = 'OBI'

print(' '.join(palavras))
