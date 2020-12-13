
quantidade = int(input())

for i in range(quantidade):
    hora, minuto, porta = map(str, input().split())

    if len(hora) == 1:
        hora = '0{}'.format(hora)
    if len(minuto) == 1:
        minuto = '0{}'.format(minuto)

    if porta == '1':        
        print('{}:{} - A porta abriu!'.format(hora, minuto))
    else:
        print('{}:{} - A porta fechou!'.format(hora, minuto))
