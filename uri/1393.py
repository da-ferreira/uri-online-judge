
while True:
    n = int(input())
    if n == 0:
        break

    termo1 = 0
    termo2 = 1

    for i in range(n):
        fib = termo1 + termo2

        termo1 = termo2
        termo2 = fib

    print(fib)
