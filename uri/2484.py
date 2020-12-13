
while True:
    try:
        palavra = list(input())

        i = 0
        while len(palavra) != 0:
            print(f'{" "  * i}{" ".join(palavra)}')
            palavra.pop(-1)
            i += 1
        print()
    except EOFError:
        break
