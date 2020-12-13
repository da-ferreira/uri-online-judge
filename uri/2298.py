
def jogada1(cartas):
    teste1 = 0

    for i in range(1, 5):
        if cartas[i] - 1 == cartas[i - 1]:
            teste1 += 1
    
    if teste1 == 4:
        return cartas[0] + 200

    return False


def jogada2(cartas):
    if cartas.count(cartas[0]) == 4:
        return cartas[0] + 180

    elif cartas.count(cartas[1]) == 4:
        return cartas[1] + 180
    
    return False


def jogada3(cartas):
    temp = [0] * 13

    for i in range(5):
        temp[cartas[i] - 1] += 1
    
    temp2 = []

    for i in range(13):
        if temp[i] == 2 or temp[i] == 3:
            temp2.append([temp[i], i + 1])

    if len(temp2) == 2:
        if temp2[0][0] == 2 and temp2[1][0] == 3:
            return temp2[1][1] + 160

        elif temp2[0][0] == 3 and temp2[1][0] == 2:
            return temp2[0][1] + 160

    return False


def jogada4(cartas):
    temp = [0] * 13

    for i in range(5):
        temp[cartas[i] - 1] += 1
    
    temp2 = []

    for i in range(13):
        if temp[i] == 3 or temp[i] == 1:
            temp2.append([temp[i], i + 1])
            
    if len(temp2) == 3:
        if temp2[0][0] == 3 and temp2[1][0] == 1 and temp2[2][0] == 1:
            return temp2[0][1] + 140

        elif temp2[0][0] == 1 and temp2[1][0] == 3 and temp2[2][0] == 1:
            return temp2[1][1] + 140

        elif temp2[0][0] == 1 and temp2[1][0] == 1 and temp2[2][0] == 3:
            return temp2[2][1] + 140

    return False


def jogada5(cartas):
    temp = [0] * 13

    for i in range(5):
        temp[cartas[i] - 1] += 1
    
    temp2 = []

    for i in range(13):
        if temp[i] == 2 or temp[i] == 1:
            temp2.append([temp[i], i + 1])
            
    if len(temp2) == 3:
        if temp2[0][0] == 2 and temp2[1][0] == 2 and temp2[2][0] == 1:
            if temp2[0][1] >= temp2[1][1]:
                return 3 * temp2[0][1] + 2 * temp2[1][1] + 20

            return 2 * temp2[0][1] + 3 * temp2[1][1] + 20

        elif temp2[0][0] == 1 and temp2[1][0] == 2 and temp2[2][0] == 2:
            if temp2[1][1] >= temp2[2][1]:
                return 3 * temp2[1][1] + 2 * temp2[2][1] + 20
            
            return 2 * temp2[1][1] + 3 * temp2[2][1] + 20

        elif temp2[0][0] == 2 and temp2[1][0] == 1 and temp2[2][0] == 2:
            if temp2[0][1] >= temp2[2][1]:
                return 3 * temp2[0][1] + 2 * temp2[2][1] + 20

            return 2 * temp2[0][1] + 3 * temp2[2][1] + 20

    return False


def jogada6(cartas):
    temp = [[0, x] for x in range(1, 14)]

    for i in cartas:
        temp[i - 1][0] += 1

    temp.sort(key=lambda k: k[0], reverse=True)

    if temp[0][0] == 2 and temp[1][0] != 2:
        return temp[0][1]
    
    return False


casos = int(input())

for i in range(casos):
    cartas = sorted(list(map(int, input().split())))

    jogadas = [
        jogada1,
        jogada2,
        jogada3,
        jogada4,
        jogada5,
        jogada6
    ]

    temp = False
    j = 0

    while temp == False and j < 6:
        temp = jogadas[j](cartas)
        j += 1
    
    print(f'Teste {i + 1}')
    
    if not temp:
        print(0)
    else:
        print(temp)
    print()
