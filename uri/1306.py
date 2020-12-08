
casos = 1

while True:
    r, n = map(int, input().split())
    if r == 0 and n == 0:
        break

    sufixos = 0

    if n < r:
        temp = n
        i = 1

        while temp < r and i <= 26:
            temp = (i * n) + n
            i += 1
        
        if temp < r:
            sufixos = 'impossible'
        else:
            sufixos = i - 1
    
    print(f'Case {casos}: {sufixos}')
    casos += 1
