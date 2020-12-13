
i = 1
while True:
    assinatura = input()
    if assinatura == '0':
        break

    if i != 1:
        print()

    painel = input()

    print('Instancia {}'.format(i))
    if assinatura in painel:
        print('verdadeira')
    else:
        print('falsa')
    i += 1
