
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    print(int((a * b * c) ** (1 / 3)))
