
entrada = list(map(int, input().split()))
entrada.sort(reverse=True)

a = entrada[0]
b = entrada[1]
c = entrada[2]

if (a < b + c) and (b < a + c) and (c < a + b):
    if a ** 2 == b ** 2 + c ** 2:
        print('r')
    elif a ** 2 < b ** 2 + c ** 2:
        print('a')
    else:
        print('o')
else:
    print('n')
