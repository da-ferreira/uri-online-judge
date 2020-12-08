
while True:
    try:
        string = list(input())
        saida = ''

        verificador = True
        for elemento in string:
            if elemento.isnumeric():
                saida += elemento
            elif elemento == 'l':
                saida += '1'
            elif elemento in 'Oo':
                saida += '0'
            elif elemento != ',' and elemento != ' ':
                print('error')
                verificador = False
                break
        
        if verificador:
            if (saida == '') or (int(saida) > 2147483647) or (int(saida) < 0):
                print('error')
            else:
                print(int(saida))
    except EOFError:
        break
