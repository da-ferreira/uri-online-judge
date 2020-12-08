
while True:
    try:
        string = input().lower().split()
        aliteracoes = 0
        temp = 0

        for i in range(1, len(string)):
            if string[i][0] == string[i-1][0]:
                temp += 1
            elif temp > 0:
                aliteracoes += 1
                temp = 0
        if temp > 0:
            aliteracoes += 1
        print(aliteracoes)
    except EOFError:
        break
