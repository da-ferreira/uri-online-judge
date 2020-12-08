
while True:
    try:
        n = int(input())
        
        botas = []
        resultado = 0

        for i in range(n):
            entrada = input().split()

            if entrada[1] == 'E' and (entrada[0] + ' D') in botas:
                resultado += 1
                botas.remove(f'{entrada[0]} D')

            elif entrada[1] == 'D' and (entrada[0] + ' E') in botas:
                resultado += 1
                botas.remove(f'{entrada[0]} E')
            else:
                botas.append(f'{entrada[0]} {entrada[1]}')
        print(resultado)
    except EOFError:
        break
