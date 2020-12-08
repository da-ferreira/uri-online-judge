
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    c = b - a

    if c > 0:
        print(a - c)
    else:
        print(a + c)
