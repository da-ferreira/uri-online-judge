
maior = 0
continuar = True
numero_anterior = []
i = 1

while True:
    try:
        numero = int(input())
        numero_anterior.append(numero)

        if i != 1:
            if numero_anterior[-2] > numero:
                continuar = False

        if numero > maior and continuar:
            maior = numero
        
        i += 1
    except:
        print(maior + 1)
        break
