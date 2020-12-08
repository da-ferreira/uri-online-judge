
i = 1
while True:
    try:
        numeracao = input()
        sapatos = input()

        f = sapatos.count(f'{numeracao} F')
        m = sapatos.count(f'{numeracao} M')

        if i != 1:
            print()

        print(f'Caso {i}:')
        print(f'Pares Iguais: {f + m}')
        print(f'F: {f}')
        print(f'M: {m}')

        i += 1
    except EOFError:
        break
