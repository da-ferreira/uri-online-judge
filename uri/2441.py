
entrada = sorted(list(map(int, input().split())))

f1 = entrada.pop(0)
f2 = entrada.pop(0)
f3 = entrada.pop(0)

area = 0

if f1 > 0:
    area += f1 * 100

if f1 + 200 < f2:
    area += (f2 - (f1 + 200)) * 100

if f2 + 200 < f3:
    area += (f3 - (f2 + 200)) * 100

if f3 + 200 < 600:
    area += (600 - (f3 + 200)) * 100

print(area)
