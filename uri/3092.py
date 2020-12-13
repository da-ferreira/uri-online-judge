
casos = int(input())

for i in range(casos):
    cartas = input()
    truco = ['Q', 'J', 'K', 'A']

    for item in cartas:
        if len(truco) > 0 and item == truco[0]:
            truco.pop(0)

    if len(truco) == 0:
        print('Agora vai')
    else:
        print('Agora apertou sem abracar')     
