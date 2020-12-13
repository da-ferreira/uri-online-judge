
casos = int(input())

for i in range(casos):
    placa = input()

    if (len(placa) != 8) or (not placa[0:3].isupper()) or (not placa[-4:].isnumeric()) or (placa[3] != '-'):
        print('FAILURE')
    else:
        if placa[-1] in '12':
            print('MONDAY')
        elif placa[-1] in '34':
            print('TUESDAY')
        elif placa[-1] in '56':     
            print('WEDNESDAY')
        elif placa[-1] in '78':
            print('THURSDAY')
        elif placa[-1] in '90':
            print('FRIDAY')
