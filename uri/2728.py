
while True:
    try:
        texto = input().split('-')
        check = 'cobol'
        veracidade = 0

        for i in range(5):
            if (texto[i][0].lower() == check[i]) or (texto[i][-1].lower() == check[i]):
                veracidade += 1

        if veracidade == 5:
            print('GRACE HOPPER')
        else:
            print('BUG')
    except EOFError:
        break
