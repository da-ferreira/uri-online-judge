
casos = int(input())

for i in range(casos):
    s1, x, s2 = input().partition('me')
    print(f'k{"a" * (s1.count("a") * s2.count("a"))}')
