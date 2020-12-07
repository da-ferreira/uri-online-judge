
salario = float(input())

juros = 0

if salario <= 2000:
    print('Isento')
else:
    salario -= 2000
    
    if salario - 1000 >= 0:
        salario -= 1000
        juros += (1000 * 0.08)

        if salario - 1500 >= 0:
            salario -= 1500
            juros += (1500 * 0.18)
            juros += (salario * 0.28)
        
        else:
            juros += (salario * 0.18)
    else:
        juros += (salario * 0.08)

    print('R$ {:.2f}'.format(juros))
