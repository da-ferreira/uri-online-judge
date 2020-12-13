
casos = int(input())

for i in range(casos):
    red = green = blue = 0

    gols = int(input())

    for j in range(gols):
        marcou, sofreu = input().split()

        if marcou == 'R':
            if sofreu == 'B':
                red += 1
            else:
                red += 2

        elif marcou == 'G':
            if sofreu == 'R':
                green += 1
            else:
                green += 2
        else:
            if sofreu == 'G':
                blue += 1
            else:
                blue += 2

    temp = [red, green, blue]

    if (red == green) and (red == blue) and (blue == green):
        print('trempate')
    elif temp.count(max(temp)) > 1:
        print('empate')
    else:
        temp = {red: 'red', green: 'green', blue: 'blue'}
        print(temp[max(temp)])
