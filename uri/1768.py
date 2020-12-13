
while True:
    try:
        tamanho = int(input())
        if tamanho % 2 == 0:
            tamanho += 1

        base1 = ' ' * ((tamanho - 3) // 2) + '***'
        base2 = ' ' * ((tamanho - 1) // 2) + '*'
        arvore = [base1, base2]

        j = 0
        for i in range(tamanho, -1, -2):
            fileira = (' ' * j) + ('*' * i)
            arvore.append(fileira)            
            j += 1

        arvore.reverse()

        for k in arvore:
            print(k)
        print()
    except EOFError:
        break
