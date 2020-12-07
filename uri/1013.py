a, b, c = input().split(' ')

a = int(a)
b = int(b)
c = int(c)

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
print('{} eh o maior'.format(maior))
