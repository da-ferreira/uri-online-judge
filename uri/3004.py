
casos = int(input())

for i in range(casos):
    a, b, c, d = map(int, input().split())

    if a > b:
        a, b = b, a
    
    if c > d:
        c, d = d, c
    
    if a < c and b < d:
        print('S')
    else:
        print('N')
