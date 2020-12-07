
while True:
    nota1 = float(input())
    while nota1 < 0 or nota1 > 10:
        print('nota invalida')
        nota1 = float(input())

    nota2 = float(input())
    while nota2 < 0 or nota2 > 10:
        print('nota invalida')
        nota2 = float(input())

    print('media = {:.2f}'.format((nota1 + nota2) / 2))

    novo = int(input('novo calculo (1-sim 2-nao)\n'))
    while novo not in range(1, 3):
        novo = int(input('novo calculo (1-sim 2-nao)\n'))
    if novo == 2:
        break
