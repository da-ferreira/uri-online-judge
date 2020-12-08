
casos = int(input())
for i in range(casos):
    valores = input().split()

    if valores[0] == '1':
        print('Case {}: {}'.format(i+1, valores[1]))
    elif valores[0] == '3':
        print('Case {}: {}'.format(i+1, valores[2]))
    elif valores[0] == '5':
        print('Case {}: {}'.format(i+1, valores[3]))
    elif valores[0] == '7':
        print('Case {}: {}'.format(i+1, valores[4]))
    elif valores[0] == '9':
        print('Case {}: {}'.format(i+1, valores[5]))
    elif valores[0] == '11':
        print('Case {}: {}'.format(i+1, valores[6]))
