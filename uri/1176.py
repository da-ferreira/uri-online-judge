
termo1 = 0
termo2 = 1
fib = 0
fibonacci = []

for i in range(61):
    fibonacci.append(fib)
    termo1 = termo2
    termo2 = fib
    fib = termo1 + termo2

casos = int(input())
for i in range(casos):
    num = int(input())
    print('Fib({}) = {}'.format(num, fibonacci[num]))
