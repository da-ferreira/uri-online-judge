
while True:
    try:
        algarismos, numero = map(str, input().split())

        numero = [int(x) for x in numero]
        numero = sum(numero)

        if numero % 3 == 0:
            print(numero, 'sim')
        else:
            print(numero, 'nao')
    except EOFError:
        break
