
while True:
    try:
        quantidade = int(input())

        estrutura = {
            'stack': 0,
            'queue': 0,
            'priority queue': 0,
            'not sure': 0,
            'impossible': False
        }

        sacola = []

        for i in range(quantidade):
            operation, elemento = map(int, input().split())

            if not estrutura['impossible']:
                if operation == 1:
                    sacola.append(elemento)

                else:
                    if elemento in sacola:
                        if sacola[-1] == elemento:
                            estrutura['stack'] += 1
                        
                        if sacola[0] == elemento:
                            estrutura['queue'] += 1
                        
                        if max(sacola) == elemento:
                            estrutura['priority queue'] += 1
                        
                        sacola.remove(elemento)
                        
                    else:
                        estrutura['impossible'] = True
        
        if estrutura['impossible']:
            print('impossible')
        else:
            temp = list(estrutura.values())
            maior = max(temp)
            temp = [x for x in temp if x == maior]

            if len(temp) == 1:
                for i in estrutura:
                    if estrutura[i] == maior:
                        print(i)

            else:
                print('not sure')
    except EOFError:
        break
