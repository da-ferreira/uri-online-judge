
agua = int(input())

if agua <= 10:
    print(7)
else:
    agua -= 10
    consumo = 7

    if (agua - 20) >= 0:
        agua -= 20
        consumo += 20

        if (agua - 70) >= 0:
            agua -= 70
            consumo += 140

            consumo += (agua * 5)
        else:
            consumo += (agua * 2)
    else:
        consumo += agua

    print(consumo)
