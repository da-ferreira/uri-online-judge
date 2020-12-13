
while True:
    try:
        pacotes = []

        comeco_do_envio = input()

        while True:
            tcp = input().split()
            if tcp[0] == '0':
                break

            pacotes.append([tcp[0], int(tcp[1])])
        
        pacotes.sort(key=lambda k: k)

        for i in range(len(pacotes)):
            print(pacotes[i][0], str(pacotes[i][1]).zfill(3))

        print()
    except EOFError:
        break
