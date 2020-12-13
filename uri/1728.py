
while True:
    equacao = input()
    parar = False

    if equacao == '0+0=0':
        parar = True

    equacao = equacao.split('+')
    a = equacao[0]
    b, c = equacao[1].split('=')

    a = int(a[-1::-1])
    b = int(b[-1::-1])
    c = int(c[-1::-1])

    if (a + b) == c:
        print('True')
    else:
        print('False')

    if parar:
        break
