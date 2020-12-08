
num = int(input())

i = 0
j = 0
while i < 1000:
    print('N[{}] = {}'.format(i, j))
    j += 1
    i += 1
    if j >= num:
        j = 0

