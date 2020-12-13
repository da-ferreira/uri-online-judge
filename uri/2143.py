
while True:
    pessoas = int(input())
    if pessoas == 0:
        break

    for i in range(pessoas):
        numero = int(input())
        if numero % 2 == 1:
            print((numero * 2) - 1)
        else:
            print((numero * 2) - 2)
