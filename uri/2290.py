
while True:
    try:
        n = int(input())
        
        numeros = sorted(list(map(int, input().split())))
        apaixonados = []

        i = 0

        while i < n - 1:
            if numeros[i] == numeros[i + 1]:
                i += 2
            
            elif numeros[i] != numeros[i + 1]:
                apaixonados.append(numeros[i])
                i += 1

        if len(apaixonados) < 2:
            apaixonados.append(numeros[-1]) 

        print(f'{apaixonados[0]} {apaixonados[1]}')
    except EOFError:
        break
