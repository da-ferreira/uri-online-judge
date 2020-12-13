
while True:
    try:
        numeros = list(map(int, input().split()))

        b, i, n, g, o = [], [], [], [], []

        k = j = 0

        while j < 5:
            if j == 2:
                b.append(numeros[k])
                i.append(numeros[k + 1])

                g.append(numeros[k + 2])
                o.append(numeros[k + 3])

                k += 4
            else:
                b.append(numeros[k])
                i.append(numeros[k + 1])
                n.append(numeros[k + 2])
                g.append(numeros[k + 3])
                o.append(numeros[k + 4])

                k += 5
            
            j += 1

        
        teste = [
            min(b) >= 1 and max(b) <= 15,
            min(i) >= 16 and max(i) <= 30,
            min(n) >= 31 and max(n) <= 45,
            min(g) >= 46 and max(g) <= 60,
            min(o) >= 61 and max(o) <= 75
        ]

        if all(teste):
            print('OK')
        else:
            numeros.sort()

            b = numeros[0:5]
            del numeros[0:5]

            i = numeros[0:5]
            del numeros[0:5]

            n = numeros[0:4]
            del numeros[0:4]

            g = numeros[0:5]
            del numeros[0:5]

            o = numeros[0:5]


            teste = [
            min(b) >= 1 and max(b) <= 15,
            min(i) >= 16 and max(i) <= 30,
            min(n) >= 31 and max(n) <= 45,
            min(g) >= 46 and max(g) <= 60,
            min(o) >= 61 and max(o) <= 75
            ]

            if all(teste):
               print('RECICLAVEL')
            else:
                print('DESCARTAVEL')
    except EOFError:
        break
