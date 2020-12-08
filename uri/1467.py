
while True:
    try:
        jogo = input()

        if jogo in '0 1 1' or jogo in '1 0 0':
            print('A')

        elif jogo in '1 0 1' or jogo in '0 1 0':
            print('B')

        elif jogo in '1 1 0' or jogo in '0 0 1':
            print('C')

        else:
            print('*')
    except:
        break

