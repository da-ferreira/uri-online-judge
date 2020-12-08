
num = int(input())
while num != 0:
    quadrados = 0
    for i in range(1, num+1):
        quadrados += i * i
    print(quadrados)
    num = int(input())
