
while True:
    inicial = int(input())
    if inicial == 0:
        break

    termo = inicial
    maior = termo

    while termo != 1:
        while termo % 2 == 1:
            termo = (3 * termo) + 1
            if termo > maior:
                maior = termo
        
        while termo % 2 == 0:
            termo = (0.5 * termo)
            if termo > maior:
                maior = termo
    
    print(int(maior))
