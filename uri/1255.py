
casos = int(input())

for j in range(casos):
    texto = input().lower()
    letras = set()

    veracidade = True

    for i in range(len(texto)):
        if texto[i].isalpha():
            if veracidade:
                maior = texto.count(texto[i])
                letras.add(texto[i])
                veracidade = False
            else:
                if texto.count(texto[i]) > maior:
                    letras.clear()
                    letras.add(texto[i])
                    maior = texto.count(texto[i])
                elif texto.count(texto[i]) == maior:
                    letras.add(texto[i])
            
    letras = list(letras)
    letras.sort()
    print(''.join(letras))
