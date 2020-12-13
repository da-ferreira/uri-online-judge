
casos = int(input())

for i in range(casos):
    a, b, c = map(int, input().split())

    delta = b ** 2 - (4 * a * c)
    altura_maxima = -delta / (4 * a)

    print(f'{altura_maxima :.2f}')
