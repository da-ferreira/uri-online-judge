
while True:
    try:
        qtd = int(input())
        lesmas = input().split()
        
        for i in range(len(lesmas)):
            lesmas[i] = int(lesmas[i])
        lesmas.sort(reverse=True)
        veloz = lesmas[0]

        if veloz < 10:
            print(1)
        elif veloz >= 10 and veloz < 20:
            print(2)
        else:
            print(3)
    except EOFError:
        break
