
while True:
    numero = input()
    if numero[0] == '-':
        break

    if len(numero) > 1 and numero[1] == 'x':
        print(int(numero, 16))
    else:
        numero = str(hex(int(numero)))
        numero = numero.upper()
        numero = numero.replace('X', 'x')
        print(numero)

