
while True:
    ficha, objetivo = input().split()
    if ficha == '*':
        break

    movimentos = 0
    i = 0    

    while i < len(ficha):
        if ficha[i] != objetivo[i]:
            i += 1

            while i < len(ficha) and ficha[i] != objetivo[i]:
                i += 1
            
            movimentos += 1
        else:
            i += 1
    
    print(movimentos)

