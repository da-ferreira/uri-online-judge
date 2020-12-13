
l, c = map(int, input().split())

x, y = map(int, input().split())

x -= 1
y -= 1

chao = []
ums = 0

for i in range(l):
    chao.append(input().split())
    ums += chao[-1].count('1')

for i in range(ums):
    if i == 0:
        if (x < l - 1) and chao[x + 1][y] == '1':
            x += 1
            direcao = 'sul'

        elif (y < c - 1) and chao[x][y + 1] == '1':
            y += 1
            direcao = 'leste'
        
        elif (x != 0) and chao[x - 1][y] == '1':
            x -= 1
            direcao = 'norte'
        
        elif (y != 0) and chao[x][y - 1] == '1':
            y -= 1
            direcao = 'oeste'
            
    else:
        if (x < l - 1) and chao[x + 1][y] == '1' and direcao != 'norte':
            x += 1
            direcao = 'sul'

        elif (y < c - 1) and chao[x][y + 1] == '1' and direcao != 'oeste':
            y += 1
            direcao = 'leste'
        
        elif (x != 0) and chao[x - 1][y] == '1' and direcao != 'sul':
            x -= 1
            direcao = 'norte'
            
        elif (y != 0) and chao[x][y - 1] == '1' and direcao != 'leste':
            y -= 1
            direcao = 'oeste'

print(x + 1, y + 1)
