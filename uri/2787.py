
l = int(input())
c = int(input())

if (l % 2 == 0) and (c % 2 == 1) or (l % 2 == 1) and (c % 2 == 0):
    print(0)
elif (l % 2 == 0) and (c % 2 == 0) or (l % 2 == 1) and (c % 2 == 1):
    print(1)
