
while True:
    try:
        n = int(input())
        filhotes = 0

        for i in range(n):
            especie = input()
            raca = input()
            nome = input().split()

            if especie == 'cachorro':
                if len(nome) > 1:

                    j = 0    
                    while j < len(nome):
                        if nome[j][0] == raca[0]:
                            filhotes += 1
                            break
                        else:
                            j += 1

            temp = input()

        print(filhotes)
    except EOFError:
        break
