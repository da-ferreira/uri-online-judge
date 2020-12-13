
b = int(input())
t = int(input())

area = ((b + t) * 70) / 2

if area < 5600.0:
    print(2)
elif area > 5600.0:
    print(1)
else:
    print(0)
