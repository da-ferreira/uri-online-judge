
while True:
    try:
        caracteres, frases = map(int, input().split())  
        caracteres1 = input()
        caracteres2 = input()
        
        frente = {}; verso = {}

        for i in range(len(caracteres1)):
            frente[caracteres1[i]] = caracteres2[i]
            verso[caracteres2[i]] = caracteres1[i]        

        for i in range(frases):
            texto = list(input())

            for j in range(len(texto)):
                if texto[j].upper() in frente:
                    if texto[j].isupper():
                        texto[j] = frente[texto[j].upper()]
                    else:
                        texto[j] = frente[texto[j].upper()].lower()
                elif texto[j].upper() in verso:
                    if texto[j].isupper():
                        texto[j] = verso[texto[j].upper()]
                    else:
                        texto[j] = verso[texto[j].upper()].lower()
            print(''.join(texto))
        print()
    except EOFError:
        break
