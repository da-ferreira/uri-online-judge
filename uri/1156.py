
s = 1
divisor = 2
for i in range(3, 40, 2):
    s += i / divisor
    divisor *= 2
print('{:.2f}'.format(s))

