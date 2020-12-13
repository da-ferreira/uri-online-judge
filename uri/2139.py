
calendario = [
    0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
]

while True:
    try:
        mes, dia = map(int, input().split())
        dias = 0
        
        for i in range(mes, 13):
            if i == mes:
                dias += (calendario[mes]) - dia
            else:
                dias += calendario[i]
        dias -= 6

        if dias == 0:
            print('E natal!')
        elif dias == 1:
            print('E vespera de natal!')
        elif dias < 0:
            print('Ja passou!')
        else:
            print(f'Faltam {dias} dias para o natal!')
    except EOFError:
        break
