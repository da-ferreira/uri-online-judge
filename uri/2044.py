
while True:
    n = int(input())
    if n < 0:
        break

    museus = list(map(int, input().split()))
    divida = 0
    result = 0

    for i in range(n):
        divida += museus[i]

        if divida % 100 == 0:
            result += 1
            divida = 0
    
    print(result)
