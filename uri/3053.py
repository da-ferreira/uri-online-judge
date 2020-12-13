
n = int(input())
posicao = input()

for i in range(n):
    banca = int(input())
    
    if (posicao == 'A' and banca == 1) or (posicao == 'C' and banca == 2):
        posicao = 'B'

    elif (posicao =='B' and banca == 2) or (posicao == 'A' and banca == 3):
        posicao = 'C'
    
    elif (posicao == 'C' and banca == 3) or (posicao == 'B' and banca == 1):
        posicao = 'A'

print(posicao)
