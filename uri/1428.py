
casos = int(input())

for i in range(casos):
    n, m = map(int, input().split())

    n //= 3
    m //= 3

    print(n * m)
