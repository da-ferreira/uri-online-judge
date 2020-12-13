
discador = {
    'ABC': '2',
    'DEF': '3',
    'GHI': '4',
    'JKL': '5',
    'MNO': '6',
    'PQRS': '7',
    'TUV': '8',
    'WXYZ': '9'
}

while True:
    try:
        telefone = input()
        telefone = telefone.replace('-', '')

        numero = ''

        for caracter in telefone:
            if caracter.isdigit() or caracter in '*#':
                numero += caracter
            elif caracter.isalpha():
                for chave in discador.keys():
                    if caracter.upper() in chave:
                        numero += discador[chave]
        print(numero)
    except EOFError:
        break
