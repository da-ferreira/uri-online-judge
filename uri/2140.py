
while True:
    compra, pago = map(int, input().split())
    if compra == 0 and pago == 0:
        break

    troco = pago - compra

    if troco > 200:
        print('impossible')
    else:
        notas = troco // 100
        temp = troco % 100

        notas += temp // 50
        temp %= 50

        notas += temp // 20
        temp %= 20

        notas += temp // 10
        temp %= 10

        notas += temp // 5
        temp %= 5

        notas += temp // 2

        if notas != 2:
            print('impossible')
        else:
            print('possible')
