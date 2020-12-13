
j = 1
while True:
    try:
        valor = int(input())
        sequencia = [0]

        for i in range(0, valor+1):
            sequencia += [i] * i
        
        print('Caso {}: {} numeros'.format(j, len(sequencia)) if len(sequencia) != 1 else 'Caso {}: 1 numero'.format(j))
        for k in range(len(sequencia)):
            if k != (len(sequencia) - 1):
                print(sequencia[k], end=' ')
            else:
                print(sequencia[k])
        print()

        j += 1
    except EOFError:
        break
