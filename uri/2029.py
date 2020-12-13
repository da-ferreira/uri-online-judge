
while True:
    try:
        volume = float(input())
        diametro = float(input())

        area = 3.14 * ((diametro / 2) ** 2)

        print(f'ALTURA = {volume / area :.2f}')
        print(f'AREA = {area :.2f}')
    except EOFError:
        break
