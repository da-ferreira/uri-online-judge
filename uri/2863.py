
while True:
    try:
        tentativas = int(input())
        corridas = []

        for i in range(tentativas):
            corridas.append(float(input()))
        print(min(corridas))

    except EOFError:
        break
