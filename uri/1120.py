
while True:
    digito, contrato = input().split()
    if digito == '0' and contrato == '0':
        break

    contrato = contrato.replace(digito, '')
    if contrato != '':
        print(int(contrato))
    else:
        print(0)
