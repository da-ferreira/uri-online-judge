
while True:
    try:
        entrada = int(input())

        if entrada in [1, 2]:
            print(entrada - 1)
        else:
            termo1 = 0
            termo2 = 1

            alterna = True

            for i in range(entrada - 2):
                if alterna:
                    phillbonati = termo1 + termo2
                    termo1 = termo2
                    termo2 = phillbonati
                    alterna = False
                else:
                    phillbonati = termo1 * termo2
                    termo1 = termo2
                    termo2 = phillbonati
                    alterna = True
                
            print(phillbonati)
    except EOFError:
        break
