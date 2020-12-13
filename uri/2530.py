
while True:
    try:
        n, m = map(int, input().split())
        juan = input().split()
        ricardinho = input().split()

        i = j = 0
        casados = m
        
        while i < n and j < m:
            if juan[i] == ricardinho[j]:
                j += 1
                casados -= 1

            i += 1

        if casados == 0:
            print('sim')
        else:
            print('nao')
    except EOFError:
        break

