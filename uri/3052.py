
def gota_escorrendo(mapa, coluna):
    for i in range(coluna):
        if mapa[0][i] == 'o':
            j = i

            while mapa[1][j] == '#':
                mapa[0][j + 1] = 'o'
                j += 1
            
            mapa[1][j] = 'o'

            j = i
                
            while mapa[1][j] == '#':
                mapa[0][j - 1] = 'o'
                j -= 1
    
            mapa[1][j] = 'o'


n, m = map(int, input().split())
mapa = []

for i in range(n):
    mapa.append(list(input()))

for i in range(n - 1):
    gota_escorrendo(mapa[i:i + 2], m)

for i in mapa:
    print(''.join(i))
