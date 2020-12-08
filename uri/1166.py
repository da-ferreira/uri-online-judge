
casos = int(input())

for i in range(casos):
    numero = int(input())

    result = 1
    progressao = 2
    j = 0

    while numero - 1 > 0:
        if result == 1:
            result += 2
            progressao += 2

            numero -= 1
        else:
            if j < 2:
                result += progressao
                j += 1

                numero -= 1
            else:
                j = 0
                progressao += 2

    print(result)
