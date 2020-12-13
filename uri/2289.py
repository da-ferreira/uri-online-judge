
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break

    x = bin(x)[2:]
    y = bin(y)[2:]

    if len(x) < len(y):
        x = x.zfill(len(y))

    elif len(x) > len(y):
        y = y.zfill(len(x))

    hamming = 0

    for i in range(len(x)):
        if x[i] != y[i]:
            hamming += 1
    
    print(hamming)

    
