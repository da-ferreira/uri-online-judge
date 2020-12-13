
casos = int(input())

for i in range(casos):
    n, m = map(int, input().split())

    if n == 1:
        result = n // m
        if result == 0:
            print(1)
        else:
            print(result)
    elif m == 1 or n == m:
        print(n // m)
    else:
        if n % m == 0:
            print(n // m)
        else:
            print((n // m) + 1)
                