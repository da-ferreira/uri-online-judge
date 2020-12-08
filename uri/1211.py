
while True:
    try:
        quantidade = int(input())
        telefones = []

        for i in range(quantidade):
            telefones.append(input())
        
        telefones.sort()

        resultado1 = 0
    
        for i in range(1, quantidade):
            j = 0

            while j < len(telefones[i]):
                if telefones[i][j] == telefones[i - 1][j]:
                    resultado1 += 1
                else:
                    break

                j += 1
        print(resultado1)             
    except EOFError:
        break
