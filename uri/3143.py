
maximo = int(input())
linhas = 0

def apagar_enters(texto):
    texto2 = []

    for i in texto:
        if i != '':
            texto2.append(i)
    
    return texto2

while True:
    try:
        texto = list(input())

        texto = apagar_enters(texto)

        if len(texto) <= maximo and len(texto) > 0:
            linhas += 1
        else:
            while len(texto) != 0:
                while texto[0] == ' ':
                    texto.pop(0)

                del texto[0:maximo]
                linhas += 1
    except:
        break

print(linhas)
