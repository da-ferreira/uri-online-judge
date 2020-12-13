
while True:
    n = int(input())
    if n == 0:
        break

    bolas_bacia = list(map(int, input().split()))
    rodadas = 0

    for i in range(n - 1, -1, -1):
        if i != 0:
            rodadas += bolas_bacia[i]

            for j in range(i - 1, -1, -1):
                bolas_bacia[j] += bolas_bacia[i]
        else:
            rodadas += bolas_bacia[0]
    
    print(rodadas)
