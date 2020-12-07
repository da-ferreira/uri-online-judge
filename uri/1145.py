
valores = input().split()
x = int(valores[0])
y = int(valores[1])
num = 1

while num <= y:
    for i in range(1, x+1):
        if i != x:
            print(num, end=' ')
        else:
            print(num)
        num += 1
