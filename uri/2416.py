
c, n = map(int, input().split())

if c > n:
    print(c % n)
elif c < n:
    print(n % c)
else:
    print(c)
