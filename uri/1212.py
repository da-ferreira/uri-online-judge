
while True:
    a, b = input().split()
    if a == '0' and b == '0':
        break
    
    a = [int(x) for x in a]
    b = [int(x) for x in b]

    while len(a) < len(b):
        a.insert(0, 0)

    while len(b) < len(a):
        b.insert(0, 0)

    carrys = 0
    
    for i in range(1, len(a) + 1,):
        if len(str(a[-i] + b[-i])) > 1:
            carrys += 1

            if len(a) != i:
                a[-(i + 1)] += 1

    if carrys == 0:
        print('No carry operation.')
    elif carrys == 1:
        print('1 carry operation.')
    else:
        print(f'{carrys} carry operations.')
