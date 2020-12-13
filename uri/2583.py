
casos =  int(input())

for i in range(casos):
    utlizacoes = int(input())

    coisas = []

    for j in range(utlizacoes):
        pedido = input().split()

        if (pedido[1] == 'chirrin') or (pedido[1] == 'chirrion'):
            if (pedido[0] not in coisas) and (pedido[1] == 'chirrin'):
                coisas.append(pedido[0])

            elif (pedido[0] in coisas) and (pedido[1] == 'chirrion'):
                coisas.remove(pedido[0])
    
    coisas.sort()

    print('TOTAL')
    for item in coisas:
        print(item)
