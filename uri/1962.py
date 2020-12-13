
casos = int(input())

for i in range(casos):
    ano = int(input())

    if ano == 2015:
        print('1 A.C.')
    else:
        if ano > 2015:
            print(f'{(ano + 1) - 2015} A.C.')
        else:
            print(f'{2015 - ano} D.C.')
    
