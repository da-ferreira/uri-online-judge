
casos = int(input())

for i in range(casos):
    tamanho = int(input())
    numeros = sorted(list(map(int, input().split())))

    numeros = [x for x in numeros if x % 2 == 1]

    alterna = True
    
    k = len(numeros) - 1
    j2 = 0

    for j in range(len(numeros)):
        if j < len(numeros) - 1:
            if alterna:
                print(numeros[k], end=' ')
                k -= 1
                alterna = False

            else:
                print(numeros[j2], end=' ')
                j2 += 1
                alterna = True
        else:
            if alterna:
                print(numeros[k])
            else:
                print(numeros[j2])
    
    if len(numeros) == 0:
        print()
