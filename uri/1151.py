num = int(input())

termo1 = 0
termo2 = 1
fibonacci = 0

for i in range(num):
    if i != (num-1):
        print('{} '.format(fibonacci), end='')
    else:
        print(fibonacci)
    termo1 = termo2
    termo2 = fibonacci
    fibonacci = termo1 + termo2
