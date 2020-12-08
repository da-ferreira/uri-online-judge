
casos = int(input())

for i in range(1, casos+1):
    numero = input().split()

    print(f'Case {i}:')

    if numero[1] == 'bin':
        print(f'{int(numero[0], 2)} dec')
        print(f'{str(hex(int(numero[0], 2)))[2:]} hex')

    elif numero[1] == 'dec':
        print(f'{str(hex(int(numero[0])))[2:]} hex')
        print(f'{str(bin(int(numero[0])))[2:]} bin')
    else:
        print(f'{int(numero[0], 16)} dec')
        print(f'{str(bin(int(numero[0], 16)))[2:]} bin')
    print()
