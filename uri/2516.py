
while True:
    try:
        s, va, vb = map(int, input().split())

        if va > vb:
            tempo = s / (va - vb)
            print(f'{tempo :.2f}')
        else:
            print('impossivel')
    except EOFError:
        break
