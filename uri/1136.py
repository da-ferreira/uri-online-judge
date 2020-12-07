
while True:
    n, b = map(int, input().split())
    if n == 0 and b == 0:
        break

    numeros_bingo = [x for x in range(n + 1)]

    bolas = list(map(int, input().split()))

    i = 0
    while len(numeros_bingo) != 0 and i < b:
        for j in range(b):
            if abs(bolas[i] - bolas[j]) in numeros_bingo:
                numeros_bingo.remove(abs(bolas[i] - bolas[j]))

        i += 1
    
    if len(numeros_bingo) == 0: 
        print('Y')
    else:
        print('N')
