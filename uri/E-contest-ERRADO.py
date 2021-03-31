
segmentos, ligacoes = map(int, input().split())

cordao = set()
ligations = []

if segmentos == 1:
    print('INCOMPLETO')
else:

    for i in range(ligacoes):
        x, y = map(int, input().split())

        if x in cordao:
            cordao.add(y)
        elif y in cordao:
            cordao.add(x)
        else:
            add = [True, None]

            for j in range(len(ligations)):
                if x in ligations[j]:
                    add[1] = j
                    add[0] = False

                    cordao.add(ligations[j][0])
                    cordao.add(ligations[j][1])
                    cordao.add(y)
                    
                
                
                elif y in ligations[j]:
                    add[1] = j
                    add[0] = False

                    cordao.add(ligations[j][0])
                    cordao.add(ligations[j][1])
                    cordao.add(x)
                
            
            if add[0]:
                ligations.append([x, y])

            else:
                ligations.pop(add[1])
        
    if len(cordao) == segmentos:
        print('COMPLETO')
    else:
        print('INCOMPLETO')

