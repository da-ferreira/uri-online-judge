
soma = 0
while True:
    num = int(input())
    if num == 0:
        break

    if num % 2 == 1:
        num += 1
    for i in range(5):
        soma += num
        num += 2

    print(soma)
    soma = 0

