
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    while len(str(n)) != 1:
        n = list(map(int, str(n)))
        n = sum(n)

    while len(str(m)) != 1:
        m = list(map(int, str(m)))
        m = sum(m)
    
    if n > m:
        print(1)
    elif n < m:
        print(2)
    else:
        print(0)
