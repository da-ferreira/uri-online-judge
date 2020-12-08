
casos = int(input())

divisores = 0
for i in range(casos):
    num = int(input())
    for j in range(1, num+1):
        if num % j == 0:
            divisores += 1

    if divisores == 2:
        print('{} eh primo'.format(num))
    else:
        print('{} nao eh primo'.format(num))

    divisores = 0
