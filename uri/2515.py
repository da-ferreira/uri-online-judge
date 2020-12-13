
while True:
    try:
        quantidade = int(input())
        bolacha = list(map(int, input().split()))

        marcos = leo = 0
        j = 0
        k = quantidade - 1

        for i in range(quantidade):
            if marcos < leo:
                marcos += bolacha[j]
                j += 1

            else:
                leo += bolacha[k]
                k -= 1    
            
        print(min(leo, marcos), max(leo, marcos))
    except EOFError:
        break
