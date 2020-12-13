
while True:
    try:
        n = int(input())

        epr = ehd = intruso = 0

        for i in range(n):
            entrada = input().split()

            if entrada[1] == 'EPR':
                epr += 1
            elif entrada[1] == 'EHD':
                ehd += 1
            else:
                intruso += 1
            
        print(f'EPR: {epr}')
        print(f'EHD: {ehd}')
        print(f'INTRUSOS: {intruso}')
    except EOFError:
        break
