
while True:
    try:
        quantidade = int(input())
        termos = input().split()

        for i in range(len(termos)):
            if termos[i] != '+':
                temp = termos[i].split('x')
                temp[0] = int(temp[0])
                temp[1] = int(temp[1])

                c = temp[0] * temp[1]
                temp[1] -= 1

                if temp[1] != 1:
                    termos[i] = f'{c}x{temp[1]}'
                else:
                    termos[i] = f'{c}x'

        print(' '.join(termos))
    except EOFError:
        break
