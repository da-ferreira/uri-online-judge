
while True:
    try:    
        n = int(input())
        carnes = []

        for i in range(n):
            entrada = input().split()
            entrada[1] = int(entrada[1])
            carnes.append(entrada)
        
        carnes = sorted(carnes, key=lambda pecas: pecas[1])
        
        for i in range(n):
            if i != (n - 1):
                print(carnes[i][0], end=' ')
            else:
                print(carnes[i][0])
    except EOFError:
        break
