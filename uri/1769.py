
while True:
    try:
        cpf = input()
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')

        soma1 = soma2 = 0

        j = 9
        for i in range(1, 10):
            soma1 += int(cpf[i - 1]) * i
            soma2 += int(cpf[i - 1]) * j
            j -= 1

        soma1 %= 11
        soma2 %= 11

        if soma1 > 9:
            soma1 = 0
        if soma2 > 9:
            soma2 = 0
        
        if soma1 == int(cpf[-2]) and soma2 == int(cpf[-1]):
            print('CPF valido')
        else:
            print('CPF invalido')
    except EOFError:
        break
