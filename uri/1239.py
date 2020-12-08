
while True:
    try:
        texto = list(input())
        italico = negrito = True

        for i in range(len(texto)):
            if texto[i] == '*':
                if negrito:
                    texto[i] = '<b>'
                    negrito = False
                else:
                    texto[i] = '</b>'
                    negrito = True
            elif texto[i] == '_':
                if italico:
                    texto[i] = '<i>'
                    italico = False
                else:
                    texto[i] = '</i>'
                    italico = True
        print(''.join(texto))
    except EOFError:
        break
