
casos = int(input())

for i in range(casos):
    number1, number2 = map(int, input().split('x'))

    for j in range(5, 11):
        if (number1 == j and number2 == j) or (number1 == number2):
            print(f'{number1} x {j} = {number1 * j}')
        else:
            print(f'{number1} x {j} = {number1 * j} && {number2} x {j} = {number2 * j}')
