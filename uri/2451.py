
tamanho = int(input())

tabuleiro = []

for i in range(tamanho):
    tabuleiro.append(input())

maior_qtd = 0
alterna = False
temp = 0

for i in range(tamanho):
    if not alterna:
        for j in range(tamanho):
            if tabuleiro[i][j] == 'o':
                temp += 1
            
            elif tabuleiro[i][j] == 'A':
                if temp > maior_qtd:
                    maior_qtd = temp
                temp = 0        

        alterna = True
    else:
        for j in range(tamanho - 1, -1, -1):
            if tabuleiro[i][j] == 'o':
                temp += 1
            
            elif tabuleiro[i][j] == 'A':
                if temp > maior_qtd:
                    maior_qtd = temp
                temp = 0

        alterna = False

if temp > maior_qtd:
    maior_qtd = temp

print(maior_qtd)
