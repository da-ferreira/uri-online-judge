
while True:
    try:
        enesimo = int(input())

        termo1 = 0
        termo2 = 1

        temp = 0

        while temp != enesimo:
            fib = termo1 + termo2

            if fib % 3 == 0 or '3' in str(fib):
                temp += 1

            termo1 = termo2
            termo2 = fib

        print(fib)
    except EOFError:
        break
