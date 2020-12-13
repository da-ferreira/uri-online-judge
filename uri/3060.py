
valor = int(input())
parcelas = int(input())

if valor % parcelas == 0:
    for i in range(parcelas):
        print(valor // parcelas)
    
else:
    for i in range(valor % parcelas):
        print((valor // parcelas) + 1)

    temp = parcelas
    parcelas -= valor % parcelas
    valor -= ((valor // temp) + 1) * (valor % temp)
    

    for i in range(parcelas):
        print(valor // parcelas)
