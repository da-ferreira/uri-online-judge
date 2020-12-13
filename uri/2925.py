
while True:
    try:
        enesimo = int(input())

        termo1 = 0
        termo2 = 1

        if enesimo == 0:
            print(0)
        elif enesimo == 1:
            print(1)
        else:
            for i in range(enesimo):
                iccanobif = termo1 + termo2

                termo1 = termo2
                termo2 = iccanobif
                
                if termo2 > 9:
                    termo2 = str(termo2)[::-1]
                    termo2 = int(termo2)

            print(iccanobif)
    except EOFError:
        break
