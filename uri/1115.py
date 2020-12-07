
while True:
    pontos = input().split()
    x = int(pontos[0])
    y = int(pontos[1])

    if x == 0 or y == 0:
        break

    if x > 0 and y > 0:
        print('primeiro')
    elif x < 0 and y > 0:
        print('segundo')
    elif x < 0 and y < 0:
        print('terceiro')
    else:
        print('quarto')
