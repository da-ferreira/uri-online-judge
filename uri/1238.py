
casos = int(input())

for i in range(casos):

    a, b = map(str, input().split())
    
    a = list(a)
    b = list(b)

    c = ''

    while (len(a) + len(b)) != 0:
        if not (len(a) == 0):
            c += a[0]
            a.pop(0)
        
        if not (len(b) == 0):
            c += b[0]
            b.pop(0)
    print(c)
