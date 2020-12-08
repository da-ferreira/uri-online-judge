
while True:
    try:
        mortos = []
        mergulharam, retornaram = map(int, input().split())

        retornados = list(map(int, input().split()))

        for i in range(1, mergulharam+1):
            if i not in retornados:
                mortos.append(i)
        
        if len(mortos) == 0:
            print('*')
        else:
            mortos.sort()
            for i in mortos:
                print(i, end=' ')
            print()
    except EOFError:
        break
