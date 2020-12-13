
vitamin_c = {
    'suco de laranja': 120,
    'morango fresco': 85,
    'mamao': 85,
    'goiaba vermelha': 70,
    'manga': 56,
    'laranja': 50,
    'brocolis': 34
}

while True:
    qtd_alimentos = int(input())
    if qtd_alimentos == 0:
        break

    vitamina = 0

    for i in range(qtd_alimentos):
        alimentos = input().split()

        vitamina += int(alimentos[0]) * vitamin_c[' '.join(alimentos[1:])]
     
    if vitamina < 110:
        print('Mais {} mg'.format(110 - vitamina))
    elif vitamina > 130:
        print('Menos {} mg'.format(vitamina - 130))
    else:
        print('{} mg'.format(vitamina))