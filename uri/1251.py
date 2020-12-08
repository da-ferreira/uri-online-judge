
from operator import itemgetter

i = 1
while True:
    try:
        caracteres = input()
        frequencia = []

        if i != 1:
            print()

        while len(caracteres) != 0:
            temp = [caracteres.count(caracteres[0]), caracteres[0]]
            caracteres = caracteres.replace(caracteres[0], '')

            frequencia.append([ord(temp[1]), temp[0]])  

        frequencia = sorted(frequencia, key=itemgetter(0), reverse=True)
        frequencia = sorted(frequencia, key=itemgetter(1))
        
        for caracter, qtd in frequencia:
            print(caracter, qtd)

        i += 1
    except EOFError:
        break
