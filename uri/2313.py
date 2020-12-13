
a, b, c = map(int, input().split())

if ((a + b) > c) and ((a + c) > b) and ((c + b) > a):

    if (a == b) and (b == c) and (a == c):
        tipo = 'Equilatero'
    elif (a != b) and (b != c) and (a != c):
        tipo = 'Escaleno'
    else:
        tipo = 'Isoceles'

    print(f'Valido-{tipo}')

    temp = [a, b, c]; maior = max(temp); temp.remove(max(temp))

    if ((temp[0] ** 2) + (temp[1] ** 2)) == maior ** 2:
        print('Retangulo: S')
    else:
        print('Retangulo: N')
else:
    print('Invalido')
