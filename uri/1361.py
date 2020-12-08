
casos = int(input())

for i in range(casos):
    quantidade = int(input())

    vermelhos = []  # negativos
    azuis = []  # positivos

    for j in range(quantidade):
        piso = int(input())

        if piso > 0:
            azuis.append(piso)
        else:
            vermelhos.append(piso)
    

    vermelhos.sort()
    azuis.sort()

    andares = []

    j = 0  # para os vermelhos
    k = len(azuis) - 1  # para os azuis
    comeco = 0

    if len(azuis) == 0:
        intercala = 'red'
    
    elif len(vermelhos) == 0:
        intercala = 'blue'
    else:

        if abs(vermelhos[j]) > azuis[k]:
            intercala = 'red'
        else:
            intercala = 'blue'

    while j < len(vermelhos) and k > -1:
        if comeco == 0:
            if intercala == 'blue':
                andares.append(azuis[k])

                k -= 1
                intercala = 'red'
                
            else:
                andares.append(abs(vermelhos[j]))

                j += 1
                intercala = 'blue'
            
            comeco += 1
        else:
            if intercala == 'blue':
                if azuis[k] < andares[-1]:
                    andares.append(azuis[k])

                    k -= 1
                    intercala = 'red'
                else:
                    k -= 1
            else:
                if abs(vermelhos[j]) < andares[-1]:
                    andares.append(abs(vermelhos[j]))

                    j += 1
                    intercala = 'blue'
                else:
                    j += 1
        

    if len(andares) == 0 and intercala == 'blue' or len(andares) == 0 and intercala == 'red':
        andares.append(0)
    else:
        if j == len(vermelhos) and intercala == 'blue':
            while k > -1:
                if azuis[k] < andares[-1]:
                    andares.append(azuis[k])
                    break
                else:
                    k -= 1
        
        elif k == -1 and intercala == 'red':
            while j < len(vermelhos):
                if abs(vermelhos[j]) < andares[-1]:
                    andares.append(abs(vermelhos[j]))
                    break
                else:
                    j += 1


    print(len(andares))
