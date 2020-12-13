
while True:
    try:
        numero = input()

        frequencia = [0] * 10

        for i in range(10):
            frequencia[i] = numero.count(str(i))

        maior = max(frequencia)

        for i in range(9, -1, -1):
            if frequencia[i] == maior:
                print(i)
                break
    except EOFError:
        break
