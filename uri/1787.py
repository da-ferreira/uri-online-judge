
from math import log2

while True:
    rodadas = int(input())
    if rodadas == 0:
        break

    pontos = [0, 0, 0]

    for i in range(rodadas):
        jogada = list(map(int, input().split()))

        for i in range(3):
            if int(log2(jogada[i])) == log2(jogada[i]):
                pontos[i] += 1
            
                if max(jogada) == jogada[i]:
                    pontos[i] += 1
            
    if pontos.count(max(pontos)) > 1:
        print('URI')    
    else:
        temp = {
            pontos[0]: 'Uilton',
            pontos[1]: 'Rita',
            pontos[2]: 'Ingred'
        }

        print(temp[max(temp)])
