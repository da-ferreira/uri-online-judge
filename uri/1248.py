
casos = int(input())

for i in range(casos):
    dieta = list(input())
    cafe_da_manha = input()
    almoco = input()

    jantar = ''
    cheater = 0

    for alimento in cafe_da_manha:
        if alimento not in dieta:
            cheater += 1 
        else:
            dieta.remove(alimento)

    for alimento in almoco:
        if alimento not in dieta:
            cheater += 1
        else:
            dieta.remove(alimento)

    if cheater != 0:
        print('CHEATER')
    else:
        dieta.sort()
        print(''.join(dieta))
