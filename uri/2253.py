
while True:
    try:
        maiuscula = minuscula = numero = 0
        validacao = True

        senha = input()

        if len(senha) < 6 or len(senha) > 32:
            print('Senha invalida.')
        else:
            for j in senha:
                if j.isnumeric():
                    numero += 1
                elif j.islower():
                    minuscula += 1
                elif j.isupper():
                    maiuscula += 1
                else:
                    print('Senha invalida.')
                    validacao = False
                    break
            if validacao:
                if (maiuscula != 0) and (minuscula != 0) and (numero != 0):
                    print('Senha valida.')
                else:
                    print('Senha invalida.')
    except EOFError:
        break
