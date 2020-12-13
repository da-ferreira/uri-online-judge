
while True:
    casos = int(input())
    if casos == 0:
        break

    for i in range(1, casos+1):
        quantidade, base1, base2 = input().split()

        sorvete = (((float(base1) + float(base2)) / 2) * 5) * int(quantidade)

        print(f'Size #{i}:')
        print(f'Ice Cream Used: {sorvete :.2f} cm2')
    print()
