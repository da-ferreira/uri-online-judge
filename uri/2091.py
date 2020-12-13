
while True:
    n = int(input())
    if n == 0:
        break

    numeros = sorted(list(map(int, input().split())))

    i = 0
    sozinho = 0

    while i < n:
        if i != n - 1 and numeros[i] == numeros[i + 1]:
            i += 2
        else:
            sozinho = numeros[i] 
            i += 1
    
    print(sozinho)
