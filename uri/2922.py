
while True:
    try:
        b, u = map(int, input().split())

        if b == u:
            print(0)
        else:
            print(abs(u - b) - 1)

    except EOFError:
        break
