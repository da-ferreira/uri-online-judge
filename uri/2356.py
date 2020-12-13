
while True:
    try:
        dna = input()
        codigo = input()

        if codigo in dna:
            print('Resistente')
        else:
            print('Nao resistente')
    except EOFError:
        break
