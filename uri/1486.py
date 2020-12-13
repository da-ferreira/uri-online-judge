
while True:
    p, n, c = map(int, input().split())
    if p == 0:
        break

    cbd = []

    for i in range(n):
        cbd.append(input().split())

    result = 0
    tamanho = 0

    for i in range(p):
        for j in range(n):
            if cbd[j][i] == '1':
                tamanho += 1
            else:
                if tamanho >= c:
                    result += 1
                tamanho = 0
        
        if tamanho > 0 and tamanho >= c:
            result += 1
        tamanho = 0
    
    print(result)
