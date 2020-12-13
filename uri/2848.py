
n, queries = map(int, input().split())

array = list(map(int, input().split()))

for i in range(queries):
    x, y, k_esimo, gugu, dabriel = map(int, input().split())
    
    temp = array[x - 1:y]
    
    temp.sort()

    k_termo = temp[k_esimo - 1]
    k_quantidade = temp.count(k_termo) 

    if abs(gugu - k_quantidade) < abs(dabriel - k_quantidade):
        vencedor = 'G'
    elif abs(gugu - k_quantidade) > abs(dabriel - k_quantidade):
        vencedor = 'D'
    else:
        vencedor = 'E'
    
    print(k_termo, k_quantidade, vencedor)
    