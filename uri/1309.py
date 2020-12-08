
while True:
    try:
        dolares = list(input())
        centavos = input()

        for i in range(len(dolares)-1, -1, -3):
            if i != (len(dolares) - 1):
                dolares.insert(i+1, ',')

        if len(centavos) == 1:
            centavos = f'0{centavos}'

        print(f'${"".join(dolares)}.{centavos}')
    except EOFError:
        break
