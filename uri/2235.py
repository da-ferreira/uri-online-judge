
c1, c2, c3 = map(int, input().split())

if (c1 == c2) or (c1 == c3) or (c2 == c3) or ((c1 + c2) == c3) or ((c1 + c3) == c2) or ((c2 + c3) == c1):
    print('S')
else:
    print('N')
