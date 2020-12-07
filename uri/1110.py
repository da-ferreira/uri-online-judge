
while True:
    numero = int(input())
    if numero == 0:
        break

    cartas = []
    for i in range(1, numero+1):
        cartas.append(i)
    
    discards = []

    while len(cartas) != 1:
        discards.append(cartas[0])
        cartas.pop(0)

        temp = cartas[0]
        cartas.pop(0)
        cartas.append(temp)

    print('Discarded cards: ', end='')
    for i in range(len(discards)):
        if i != (len(discards) - 1):
            print(discards[i], end=', ')
        else:
            print(discards[i])
    
    print('Remaining card: {}'.format(cartas[0]))
