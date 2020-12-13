
casos = int(input())

for i in range(casos):
    c, d = map(int, input().split())

    if c == 0 and d != 0:
        print(10 ** d)
    elif d == 0 and c != 0:
        print(26 ** c)
    elif c == 0 and d == 0:
        print(0)
    else:
        print((26 ** c) * (10 ** d))
